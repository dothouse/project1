# 첫번째 project

## 팀
- 팀 이름 : 꿀먹은 한라산 <br>
- 구성원 :강민서, 김제이, 송진석, 유지현, 조신호

## 주제
제주도 한달살기 관광/숙박지역 선택을 위한 추천시스템 구현 

## 목적

 - 제주도에서 한 달 살기 하는 여행객들이 증가함에 따라 숙박 및 편의 시설에 대한 정보 부족이 문제점으로 대두. 이 문제를 해결하고 여행객들에게 도움을 주기 위한 효과적인 시스템을 구축하려고 함

 - 한 달 살기 여행객들은 각자 다양한 여행 패턴을 보이고 이를 반영하여 선호하는 관광 유형에 맞는 숙소, 주변 편의 시설, 관광지, 맛집 등의 데이터를 기반으로 한 의사 결정 지원이 필요

 - 사용자 친화적인 웹 페이지를 구축하여 서비스에 쉽게 접근할 수 있도록 하고, 숙소 주변의 지도를 제공하여 숙소 및 주변 시설의 위치 직관적으로 확인 가능


## 프로젝트 수행방안

1.	데이터 수집
    - 공공데이터 – 지역의 공공기관, 생활시설, 기후, 교통, 관광지 등 정보 수집
    - 웹 크롤링 – 관광지, 숙소 등 주관적인 요소가 반영되는 요인, 공공데이터에서 확인 불가능한 생활시설 정보 수집

2.	데이터 전처리
    - 정형데이터 – 이상치, 결측치 등을 확인
    - 비정형데이터 – 자연어 분석을 위한 전처리
    - Geodata – 서비스 구현시 지도에 표현하기 위한 준비

3.	데이터 분석
    - 토픽모델링을 통한 기존 여행자들의 여행 패턴 확인
    - 기존 여행자 패턴을 바탕으로 관광지, 기후, 등 다양한 한달살기에 필요한 정보 clustering
    - 관광정보 이외의 다양한 생활편의시설에 대한 분석    
    - 한달살기에 적합한 지역 추천

4.	서비스 구현 및 시각화
    - 분석된 결과를 토대로 희망하는 여행유형에 따라 숙소 및 관광지 추천
    - Python, Flask를 활용한 웹서비스 개발
    - 지도를 활용한 시각화

## 프로젝트 수행 일정

1.	기획 및 데이터 수집(~ 2024/1/13)
    - 프로젝트 주제 선정 및 아이디어 발표
    - 기획안 작성
    - 데이터 수집 (크롤링, 공공데이터 등) 
    - 전원
2.	데이터 전처리(~ 2024/1/18)
    - 비정형 데이터 – 송진석, 유지현
    - 정형 데이터 – 강민서, 김제이, 조신호
    - API 활용 주소 정보 확인 - 전원
3.	데이터 분석 및 시각화(~ 2024/1/21)
    - 비정형 데이터 – 송진석, 유지현
    - Geodata 시각화 - 강민서, 김제이, 조신호
    - 그래프 시각화(EDA) - 강민서, 김제이    
4.	서비스 구현 및 발표 준비(~ 2024/1/23)
    - 데이터 통합 및 웹 서비스 구현 - 송진석
    - PPT 제작 - 강민서, 김제이, 유지현, 조신호
    - 피드백 의견 반영하여 프로젝트 고도화 - 전원    
5. 프로젝트 발표(2024/1/24)
    - 발표 - 김제이, 유지현


## 업무 분담

1. 강민서
    - 데이터 수집 - 생활필수시설(경찰서, 마트, 병원, 약국, 은행), 기념품 샵
    - 데이터 분석 및 시각화(EDA, 지도)
    - ppt 제작

2. 김제이
    - 데이터 수집 - 기상데이터, 맛집
    - 데이터 분석 및 시각화(EDA, 지도)
    - 데이터 통합
    - 발표
3. 송진석
    - 데이터 수집 - 한달살기 후기, 숙소 정보
    - 데이터 분석 및 시각화(EDA, 텍스트 분석)
    - 데이터 통합
    - 웹구현
4. 유지현
    - 데이터 수집 - 관광정보(visit jeju)
    - 데이터 분석 및 시각화(EDA, 텍스트 분석)
    - 발표
5. 조신호
    - 데이터 수집 - 관광정보(오름, 올레길)
    - 데이터 분석 및 시각화(EDA, 지도)


## 데이터

1. 크롤링

- mrmention - 제주도 한달살기 숙소 분석을 위한 사이트
    https://www.mrmention.co.kr/
- naver blog - 제주도 한달살기 후기 확인
- visit jeju - 제주도 관광지 정보
- kakao 지도 - 생활필수시설(경찰서, 마트, 병원, 약국, 은행), 기념품 샵, 맛집

2. 공공데이터

- 기상청 - 기상자료
- 미세먼지 - 미세먼지
- 공공데이터 포털 -  오름, 올레길
- 제주관광공사 - 맛집

3. geodata

- Kakao map api - 좌표, 행정동 등

## 수행도구

-	웹 크롤링: python / beautiful soup, selenium, pandas, numpy
-	데이터분석 및 시각화: python / pandas, numpy, matplotlib, seaborn, folium
-	서비스 구현: html, css, javascript, python / Flask
-	협업: Github, 구글드라이브


## 폴더구조
1. data - 수집데이터
2. result - EDA, 시각화, 텍스트 분석 결과
3. step1_data_collection - 데이터 수집(crwaling)
4. step2_preprocessing - 데이터 전처리
5. step3_analysis - 시각화, 지도, 텍스트 분석
6. step4_data_integration - 데이터 통합 및 정리
7. web - 웹구현
