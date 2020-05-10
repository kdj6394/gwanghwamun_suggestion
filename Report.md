# Report
## data
1. 데이터는 crawling 된 데이터를 사용함.
2. crawling 시각은 2020-05-09, 18 : 04 을 기준으로 함.

## analysis
* 구분별 청원횟수
    1. 데이터의 구분목록(보건의료,공공행정,교육,기타 등...)을 추출하여 각 값을 count 후 그래프 생성
    2. ![이미지](https://github.com/kdj6394/Gwanghwamun_Suggestion/blob/master/src/img/%EA%B5%AC%EB%B6%84%EB%B3%84%EC%B2%AD%EC%9B%90%ED%9A%9F%EC%88%98.png?raw=true)
    3. 확인결과 기타가 501로 가장 높으며, 다음으로 보건의료,공공행정,사회복지 등이 등장,가장 낮은 부분은 통일외교로 6건 밖에 해당하지 않음 


* 진행상황별 목록
    1. 데이터의 진행상황(토론종료,토론중,숙성중,과제추친중,숙성종료)을 추출하여 각 값을 count 후 그래프 생성
    2. ![이미지](https://github.com/kdj6394/Gwanghwamun_Suggestion/blob/master/src/img/%EC%A7%84%ED%96%89%EC%83%81%ED%99%A9%EB%B3%84%EB%AA%A9%EB%A1%9D%ED%9A%9F%EC%88%98.png?raw=true)

* 생성날짜별 청원횟수
    1. 데이터의 생성날짜(2018-10-30 ~ 2020-05-09)를 추출하여 각 값을 count 후 그래프 생성
    2. ![이미지](https://github.com/kdj6394/Gwanghwamun_Suggestion/blob/master/src/img/%EC%83%9D%EC%84%B1%EB%82%A0%EC%A7%9C%EB%B3%84%EC%B2%AD%EC%9B%90%ED%9A%9F%EC%88%98.png?raw=true)
    
    3. 청원횟수가 20회 이상인 날은 다음과 같다. 20회인 이상의경우 날짜별 word cloud 를 생성함. 
    4. 
        |생성날짜목록 | 청원횟수|
        |:----:|----:|
        |2018-10-30 |    97|
        |2019-03-04 |   100|
        |2019-03-05 |    56|
        |2019-03-30 |    54|
        |2019-04-30 |    63|
        |2019-10-10 |    45|
        |2019-10-11 |    22|
        |2019-11-21 |    44|
        |2020-02-26 |    24|
        |2020-03-31 |    51|
        |2020-04-01 |   120|
        |2020-04-04 |    45|
        |2020-05-06 |    21|

 * 구분별 좋아요수
    1. 데이터의 구분별 좋아요수를 추출하여 각 값을 count 후 그래프 생성
    2. ![이미지](https://github.com/kdj6394/Gwanghwamun_Suggestion/blob/master/src/img/%EA%B5%AC%EB%B6%84%EB%B3%84%EC%A2%8B%EC%95%84%EC%9A%94%EC%88%98.png?raw=true)
    3. 각 구분별 좋아요수의 mean 과 max는 아래와 같다.
    4. 
        | 구분 | Mean | Max |
        |:----:|----:|----:|
        |공공행정|      0.981|        40|
        |과학기술|      0.722|        10|
        |교육|          2.244|        29|
        |교통물류|      2.158|        47|
        |국토관리|      0.750|         4|
        |기타|          2.665|       164|
        |농축수산|      0.867|         5|
        |문화관광|      9.900|        83|
        |보건의료|     10.316|       757|
        |사회복지|      6.045|       269|
        |산업고용|      2.102|        42|
        |식품건강|      2.933|        33|
        |재난안전|      1.604|        40|
        |재정금융|      1.310|        33|
        |통일외교|      0.500|         1|
        |환경기상|      1.070|         5| 

## word_cloud
all_word_cloud ![이미지](https://github.com/kdj6394/Gwanghwamun_Suggestion/blob/master/src/img/all_word_cloud.png?raw=true)
