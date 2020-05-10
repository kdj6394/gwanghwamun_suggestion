# gwanghwamun_suggestion
## 개요
* 청와대 국민청원 :  문재인 정부 출범 이후 청와대 웹사이트에서 국민이 청원을 제시하여 SNS 계정으로 로그인한 20만 명의 추천을 받으면 책임자가 답변을 하는 제도이다. 이 제도에서 등장하고 토론한 안건을 살펴본다.

## 순서
1. 데이터의 수집(크롤링 및 저장)
2. 데이터의 분석(통계 및 시각화)

### requirements
* pip install -r requirements.txt 
* KoNLPy - 설치참고(https://konlpy.org/ko/latest/install/)

### path
* Crawling
    1. driver_path : __Users\chromedriver.exe__
    2. data_save_path : __Users\data__

    
* Analysis_path
    1. root : __Users\data__ (folder)


* word_cloud_path : 
    1. root : __Users\data__ (folder)
    2. img_path : __Users\setting\img__ (jpg,png ..)
    3. font_path : __Users\setting\font__ (tiff)

### 데이터출처
* 광화문1번가(https://www.gwanghwamoon1st.go.kr/front/main/index.do)
* 정책제안 -> 혁신제안톡 -> 전체
