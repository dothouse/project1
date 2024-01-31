# def mapping(category, color, icon):
#     globals()[str(category) + '_detail'] = db.session.query(category).all()
#     temp_detail = globals()[str(category) + '_detail']
#
#     for i in range(len(temp_detail)):
#         folium.Marker(
#             location=[temp_detail[i].lat, temp_detail[i].lng],
#             tooltip=temp_detail[i].name,  # 마커에 마우스를 올렸을 때 표시되는 툴팁으로 병원명 표시
#             popup=folium.Popup(temp_detail[i].addr, max_width=200),
#             icon=folium.Icon(color= color, icon= icon)
#         ).add_to(pension_map)
#
# mapping(Hospital, 'red', 'glyphicon-heart-empty')
# mapping(Parm, 'red', 'glyphicon-plus')
# mapping(Mart, 'purple', 'glyphicon-shopping-cart')
# mapping(Bank, 'red', 'glyphicon-usd')
# mapping(Police, 'blue', 'glyphicon-map-marker')

# hospital_distance = []
# for i in range(len(hospital_detail)):
#     start = (hospital_detail[i].lat, hospital_detail[i].lng)
#     name = hospital_detail[i].name
#     addr = hospital_detail[i].addr
#     sun = hospital_detail[i].sun
#     haver = haversine(start, goal)
#     hospital_distance.append([name, haver, addr, sun])
# hospital_distance = pd.DataFrame(hospital_distance)
# hospital_distance.columns = ['name', 'haver', 'addr', 'sun']
# hospital_distance_list = hospital_distance['haver'].sort_values(ascending=True)
#
# near_hospital_distance = hospital_distance_list.head(1).values[0]
# near_hospital = hospital_distance[hospital_distance['haver'] == near_hospital_distance]


def cal_distance(category):
    goal = (pension_lat, pension_lng)
    temp_distance = []
    temp_detail = globals()[str(category) + '_detail']
    for i in range(len(temp_detail)):
        start = (temp_detail[i].lat, temp_detail[i].lng)
        name = temp_detail[i].name
        addr = temp_detail[i].addr
        sun = temp_detail[i].sun
        haver = haversine(start, goal)
        temp_distance.append([name, haver, addr, sun])
    temp_distance = pd.DataFrame(temp_distance)
    temp_distance.columns = ['name', 'haver', 'addr', 'sun']
    temp_distance_list = temp_distance['haver'].sort_values(ascending=True)
    near_temp_distance = temp_distance_list.head(1).values[0]
    globals()['near' + str(category)] = temp_distance[temp_distance['haver'] == near_temp_distance]

    type1 = db.session.query(TestData).join(selected_query, selected_query.pensionID == TestData.pensionID).filter(TestData.type == 1 ).all()
    type2 = db.session.query(TestData).join(selected_query, selected_query.pensionID == TestData.pensionID).filter(TestData.type == 2).all()
    type3 = db.session.query(TestData).join(selected_query, selected_query.pensionID == TestData.pensionID).filter(TestData.type == 3).all()
    type4 = db.session.query(TestData).join(selected_query, selected_query.pensionID == TestData.pensionID).filter(TestData.type == 4).all()




    <div class = 'container'>
        <p>숙소 이름 {{ pension_name }}</p> <br>
        <p>지역 -> {{ pension_detail[0].location}}</p>
        <p>주소 -> {{ pension_detail[0].addr}} </p>
        <p>가격 -> {{ pension_detail[0].price }}</p>
        <p>평점 -> {{ pension_detail[0].rating}}</p>

        <p>숙소시설</p>
        <ul>
            <li>시설1 - {{ pension_detail[0].ammen1}}</li>
            <li>시설2 - {{ pension_detail[0].ammen2}}</li>
            <li>시설3 - {{ pension_detail[0].ammen3}}</li>
            <li>시설4 - {{ pension_detail[0].ammen4}}</li>
            <li>시설5 - {{ pension_detail[0].ammen5}}</li>
        </ul>
        <p>숙소주변 편의시설</p>
        <ul>
            <li> 가장 가까운 병원 : {{ near_hospital.name.values[0]}} - {{ near_hospital.addr.values[0]}} / 직선거리 {{ near_hospital.haver.values[0]}}Km</li>
            <li> 가장 가까운 병원(일요일) : {{ near_hospital_sun.name.values[0]}} - {{ near_hospital_sun.addr.values[0]}} / 직선거리 {{ near_hospital_sun.haver.values[0]}}Km</li>
            <li> 가장 가까운 약국 : {{ near_parm.name.values[0]}} - {{ near_parm.addr.values[0]}} / 직선거리 {{ near_parm.haver.values[0]}}Km</li>
            <li> 가장 가까운 마트 : {{ near_mart.name.values[0]}} - {{ near_mart.addr.values[0]}} / 직선거리 {{ near_mart.haver.values[0]}}Km</li>
            <li> 가장 가까운 경찰서 : {{ near_police.name.values[0]}} - {{ near_police.addr.values[0]}} / 직선거리 {{ near_police.haver.values[0]}}Km</li>
        </ul>

    </div>

for i in range(1, 5):
    globals()['type' + str(i)] = (db.session.query(TestData).join(Pension, TestData.pensionID == Pension.pensionID)
                                  .filter(TestData.type == 1).filter(
        Pension.pensionID.in_(result_pensionID_list)).all())

temp_list = []
for i in range(len(type1)):
    name = type1[i].pensionID

    hospital = type1[i].cnt_3km
    parm = type2[i].cnt_3km  # parm은 따로 조사하지 않음 - 약국과 연동
    mart = type3[i].cnt_5km
    bank = type4[i].cnt_15km

    bbb = 1

    score = (hospital * select_value.hospital + parm * select_value.hospital +
             mart * select_value.mart + bank * select_value.bank + bbb)
    temp_list.append([name, int(score), int(hospital), int(parm), int(mart), int(bank)])

test_df = pd.DataFrame(temp_list)
test_df.columns = ['name', 'score', 'hospital', 'parm', 'mart', 'bank']
test_df.sort_values(by='score', ascending=False, inplace=True)
score_list = test_df['score'].sort_values(ascending=False)