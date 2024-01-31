import pandas as pd

from flask import Blueprint, render_template, request

import folium

from haversine import haversine

from jeju import db
from jeju.models import selectData, Pension, Hospital, Police, Mart, Bank, Parm


bp = Blueprint('pension', __name__, url_prefix='/select')

@bp.route('/pension', methods=('GET', 'POST'))
def choice_pension():

    pension_name = request.form['pension_name']
    pension_detail = db.session.query(Pension).filter(Pension.pensionID == pension_name).all()

    pension_lat = pension_detail[0].latitude
    pension_lng = pension_detail[0].longitude

    pension_map = folium.Map(location=[pension_lat, pension_lng], zoom_start=14)

    pension_map.get_root().width = "100%"
    pension_map.get_root().height = "800px"

    # 숙소 위치 mapping
    folium.Marker([pension_lat, pension_lng],
                  tooltip=pension_detail[0].addr,
                  icon = folium.Icon(icon= 'glyphicon-home', color= 'darkblue')).add_to(pension_map)
    folium.Circle([pension_lat, pension_lng], radius= 200,
                  color='red',  # Specify the fill color here
                  fill=True,
                  fill_color='red',  # You can set this to a different color if needed
                  fill_opacity=0.7,
                  ).add_to(pension_map)

    # haversine 거리계산의 중심
    goal = (pension_lat, pension_lng)

    # 일요일 병원
    hospital_detail = db.session.query(Hospital).all()
    hospital_sun_distance = []
    for i in range(len(hospital_detail)):
        if hospital_detail[i].sun == 1:
            start = (hospital_detail[i].lat, hospital_detail[i].lng)
            name = hospital_detail[i].name
            addr = hospital_detail[i].addr
            sun = hospital_detail[i].sun
            haver = haversine(start, goal)
            haver = round(haver, 2)
            hospital_sun_distance.append([name, haver, addr, sun])
    hospital_sun_distance = pd.DataFrame(hospital_sun_distance)
    hospital_sun_distance.columns = ['name', 'haver', 'addr', 'sun']
    hospital_sun_distance_list = hospital_sun_distance['haver'].sort_values(ascending=True)

    near_hospital_sun_distance = hospital_sun_distance_list.head(1).values[0]
    near_hospital_sun = hospital_sun_distance[hospital_sun_distance['haver'] == near_hospital_sun_distance]



    # 거리 계산하는 함수1
    def category_mapping(category, color, icon):
        goal = (pension_lat, pension_lng)
        globals()[str(category)+ '_detail'] = db.session.query(category).all()
        temp_distance = []
        temp_detail = globals()[str(category) + '_detail']
        for i in range(len(temp_detail)):
            start = (temp_detail[i].lat, temp_detail[i].lng)
            name = temp_detail[i].name
            addr = temp_detail[i].addr
            haver = haversine(start, goal)
            haver = round(haver, 2)
            temp_distance.append([name, haver, addr])

            # mapping
            if haver < 10:
                folium.Marker(
                    location=[temp_detail[i].lat, temp_detail[i].lng],
                    tooltip=temp_detail[i].name,  # 마커에 마우스를 올렸을 때 표시되는 툴팁으로 병원명 표시
                    popup=folium.Popup(temp_detail[i].addr, max_width=200),
                    icon=folium.Icon(color=color, icon=icon)
                ).add_to(pension_map)

        temp_distance = pd.DataFrame(temp_distance)
        temp_distance.columns = ['name', 'haver', 'addr']
        temp_distance_list = temp_distance['haver'].sort_values(ascending=True)
        near_temp_distance = temp_distance_list.head(1).values[0]

        return  temp_distance[temp_distance['haver'] == near_temp_distance]

    #  마커 - 가능한 색상 'red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue',
    #  'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray'
    near_hospital = category_mapping(Hospital, 'orange', 'glyphicon-map-marker')
    near_police = category_mapping(Police, 'blue', 'glyphicon-user')
    near_mart = category_mapping(Mart, 'purple', 'glyphicon-shopping-cart')
    near_bank = category_mapping(Bank, 'red', 'glyphicon-usd')
    near_parm = category_mapping(Parm, 'green', 'glyphicon-plus')

    # iframe에 pension_map 할당
    iframe = pension_map.get_root()._repr_html_()

    return render_template('select_info/pension_info.html',
                            pension_name = pension_name, pension_detail = pension_detail, iframe=iframe,
                           near_hospital=near_hospital, near_hospital_sun=near_hospital_sun,
                           near_police=near_police, near_mart=near_mart, near_bank=near_bank,
                           near_parm=near_parm)

