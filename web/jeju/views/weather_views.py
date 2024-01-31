from flask import Blueprint, render_template, request

import pandas as pd
from haversine import haversine

## 그림을 위한 패키지
from io import BytesIO, StringIO
import base64

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

from jeju import db
from jeju.models import Pension
from jeju.models import Weather, Weather_point, Pm_point, Pm

bp = Blueprint('weather', __name__, url_prefix='/info')

@bp.route('/weather', methods=('GET', 'POST'))
def weather():
    pension_name = request.form['finalPension']
    pension_detail = db.session.query(Pension).filter(Pension.pensionID == pension_name).all()

    pension_lat = pension_detail[0].latitude
    pension_lng = pension_detail[0].longitude

    query_wp = db.session.query(Weather_point).all()
    query_pp = db.session.query(Pm_point).all()

    def weather_haver(df):
        goal = (pension_lat, pension_lng)
        temp_distance = []
        for i in range(len(df)):
            start = (df[i].lat, df[i].lng)
            name = df[i].name
            addr = df[i].addr
            haver = haversine(start, goal)
            haver = round(haver, 2)
            temp_distance.append([name, haver, addr])

        temp_distance = pd.DataFrame(temp_distance)
        temp_distance.columns = ['name', 'haver', 'addr']
        return pd.DataFrame(temp_distance)

    def select_near(df):
        temp_distance_list = df['haver'].sort_values(ascending=True)
        near_temp_distance = temp_distance_list.head(1).values[0]
        temp = df[df['haver'] == near_temp_distance]
        return pd.DataFrame(temp)

    wp_haver = weather_haver(query_wp)
    wp_haver_short = select_near(wp_haver)

    pm_haver = weather_haver(query_pp)
    pm_haver_short = select_near(pm_haver)

    wp_spot = wp_haver_short.name.values[0]
    weather_detail = db.session.query(Weather).filter(Weather.point_name == wp_spot).all()

    # pp_spot은 html에서 사용했지만 pm_detail은 사용하지 못했다.
    pp_spot = pm_haver_short.name.values[0]
    pm_detail = db.session.query(Pm.day, Pm.year)

    return render_template('weather/weather.html',
                           wp_haver=wp_haver, wp_haver_short=wp_haver_short,
                           pm_haver=pm_haver, pm_haver_short=pm_haver_short,
                           weather_detail=weather_detail, pm_detail=pm_detail)


# 파이썬 코드로 실행시켜서 그래프를 그리고 html에서 나타내기
# <img src="data:image/jpeg;base64,{{ img_data }}"> 와 연동
# https://frhyme.github.io/python-lib/flask_matplotlib/
@bp.route('/weather/<point>', methods=('GET', 'POST'))
def weather_fig(point):
    if 'wp_name' in request.form:
        point = request.form['wp_name']
        selected_query = db.session.query(Weather).filter(Weather.point_name == point).all()
    elif 'pm_name' in request.form:
        point = request.form['pm_name']
        selected_query = db.session.query(Pm).filter(Weather.point_name == point).all()
    else:
        point = 'none'
        selected_query = 'none'

    # Weather Query를 필요한 column만 빼서 DataFrame으로 만들기
    selected_query = db.session.query(Weather).filter(Weather.point_name == point).all()
    temp_list = []
    for i in range(len(selected_query)):
        point_name = selected_query[i].point_name
        date = selected_query[i].date
        temperature = selected_query[i].temperature
        rain = selected_query[i].rain
        temp_list.append({'point_name': point_name,
                          'date': pd.to_datetime(date),
                          'temperature': temperature,
                          'rain': rain})
    df_weather = pd.DataFrame(temp_list)
    df_weather['date'] = pd.to_datetime(df_weather['date'], format='%Y-%M-%d')
    df_weather['date'] = df_weather['date'].dt.strftime('%y-%m-%d')
    df_weather['date'] = pd.to_datetime(df_weather['date'], format='%y-%m-%d')

    # 추출된 데이터를 토대로 matplotlib을 통해서 그래프화
    df_graph = df_weather[df_weather['date'] > '2022-12-31']
    plt.figure(figsize=(10, 5))
    plt.title(f"{point} 관측소 정보", fontsize=15)
    plt.plot(df_graph["date"], df_graph["temperature"], "-", color='orange', label=str(point))
    plt.grid()
    plt.legend(fontsize=13)
    plt.xticks(rotation=45)

    # 그래진 그래프를 텍스트 형태로 저장하여 decode
    img = BytesIO()
    plt.savefig(img, format='png', dpi=200)
    img.seek(0)
    img_str = base64.b64encode(img.read()).decode('utf-8')

    return render_template("weather/show_weather.html", img_data=img_str)

    # return send_file(img, mimetype='image/png')


@bp.route('/pm/<point>', methods=('GET', 'POST'))
def pm_fig(point):
    if 'pm_name' in request.form:
        point = request.form['pm_name']
        selected_column = getattr(Pm, point)
        selected_query = db.session.query(Pm.date, selected_column).all()
    else:
        point = 'none'
        selected_query = 'none'

    pm_list = []
    for i in range(len(selected_query)):
        date = selected_query[i][0]
        date = pd.to_datetime(date)
        pm = selected_query[i][1]
        pm_list.append({'date': date,
                        'pm': pm})
    df_pm = pd.DataFrame(pm_list)
    df_pm['date'] = pd.to_datetime(df_pm['date'], format='%Y-%M-%d')
    df_pm['date'] = df_pm['date'].dt.strftime('%y-%m-%d')
    df_pm['date'] = pd.to_datetime(df_pm['date'], format='%y-%m-%d')

    df_pm2 = df_pm[(df_pm['date'] > '2023-01-01') & (df_pm['date'] < '2024-01-01')]
    plt.figure(figsize=(10, 5))
    plt.title(f"{point} 관측소 - 미세먼지", fontsize=15)
    plt.plot(df_pm2["date"], df_pm2["pm"], "-", color='orange', label=str(point))
    plt.grid()
    plt.legend(fontsize=13)
    plt.xticks(rotation=45)
    img = BytesIO()
    plt.savefig(img, format='png', dpi=200)
    img.seek(0)
    img_str = base64.b64encode(img.read()).decode('utf-8')

    return render_template("weather/show_pm.html", test=df_pm['date'].dtype, img_data=img_str)
