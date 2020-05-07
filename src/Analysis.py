from lib import os,glob,sys,join,basename,dirname
from lib import np,pd,plt,sns
from lib import WordCloud,Image,ImageColorGenerator,Komoran,nltk
from lib import Okt
plt.rc('font',family='Malgun Gothic')


if __name__ == '__main__':
    # root = r'C:\Users\82104\Documents\GitHub\Gwanghwamun_Suggestion\data'
    root = r'C:\ProgramData\Anaconda3\kdj\Git\Gwanghwamun_Suggestion\data'
    img_save_root = join(dirname(root),'src','Analysis_img')
    os.makedirs(img_save_root,exist_ok=True)

    data_path = glob.glob(join(root,'*.txt'))[-1]
    data = pd.read_csv(data_path,sep='\t',header=None,encoding='utf8')
    
    data.columns = ['구분','진행상황','생성날짜','ID','좋아요수','제목','내용']
    
    division_df = pd.DataFrame(data['구분'])
    unique_list = division_df['구분'].unique()
    value = division_df['구분'].value_counts()
    division_df_count = division_df['구분'].value_counts().rename_axis('구분목록').reset_index(name='청원횟수')
    division_df_count = division_df_count.sort_values(by=['청원횟수'], ascending = True).reset_index()

    plt.figure(figsize=(15,8))
    plt.xlabel('구분목록')
    plt.ylabel('청원횟수')
    plt.title('구분목록 별 청원횟수',fontsize=15)
    plt.barh(division_df_count['구분목록'],division_df_count['청원횟수'],label='청원횟수')
    for i,v in enumerate(division_df_count['구분목록']):
        str_val = division_df_count['청원횟수'][i]
        plt.text(division_df_count['청원횟수'][i],v,str_val,
                fontsize=9,color='red',horizontalalignment = 'left',
                verticalalignment = 'center',fontweight='bold')
    plt.grid()
    plt.draw()
    fig = plt.gcf()
    fig.savefig(join(img_save_root,'구분별청원횟수.png'),dpi=fig.dpi)

    '''확인결과 기타가 467로 가장 높으며, 다음으로 보건의료,공공행정,사회복지 등이 등장함
    가장 낮은 부분은 통일외교로 7건 밖에 해당하지 않음
    '''
    
    situation_df = pd.DataFrame(data['진행상황'])
    unique_list = situation_df['진행상황'].unique()
    value = situation_df['진행상황'].value_counts()
    situation_df_count = situation_df['진행상황'].value_counts().rename_axis('진행상황목록').reset_index(name='목록횟수')
    situation_df_count = situation_df_count.sort_values(by=['목록횟수'], ascending = True).reset_index()

    plt.figure(figsize=(15,8))
    plt.xlabel('진행상황목록')
    plt.ylabel('목록횟수')
    plt.title('진행상황목록 별 목록횟수',fontsize=15)
    plt.barh(situation_df_count['진행상황목록'],situation_df_count['목록횟수'],label='목록횟수')
    for i,v in enumerate(situation_df_count['진행상황목록']):
        str_val = situation_df_count['목록횟수'][i]
        plt.text(situation_df_count['목록횟수'][i],v,str_val,
                fontsize=9,color='red',horizontalalignment = 'left',
                verticalalignment = 'center',fontweight='bold')
    plt.grid()
    plt.draw()
    fig = plt.gcf()
    fig.savefig(join(img_save_root,'진행상황별목록횟수.png'),dpi=fig.dpi)


    date_df = pd.DataFrame(data['생성날짜'])
    unique_list = date_df['생성날짜'].unique()
    value = date_df['생성날짜'].value_counts()
    date_df_count = date_df['생성날짜'].value_counts().rename_axis('생성날짜목록').reset_index(name='청원횟수')
    date_df_count = date_df_count.sort_values(by=['생성날짜목록'], ascending = True).reset_index()

    plt.figure(figsize=(15,8))
    plt.xlabel('생성날짜목록')
    plt.ylabel('청원횟수')
    plt.title('생성날짜목록 별 청원횟수',fontsize=15)
    plt.plot(date_df_count['생성날짜목록'],date_df_count['청원횟수'],'-',label='청원횟수')
    plt.xticks(fontsize=7,rotation=65)
    for i,v in enumerate(date_df_count['청원횟수']):
        str_val = date_df_count['생성날짜목록'][i]
        plt.text(date_df_count['생성날짜목록'][i],v,str_val,fontsize=8,color='black',
        horizontalalignment = 'left',verticalalignment = 'center',fontweight = 'bold')
    plt.draw()
    fig = plt.gcf()
    fig.savefig(join(img_save_root,'생성날짜별청원횟수.png'),dpi=fig.dpi)

    ''' 청원횟수가 20회가 넘어가는 날은 다음과 같다.
        생성날짜목록  청원횟수
        2018-10-30    67
        2019-03-04   100
        2019-03-05    56
        2019-04-30    62
        2019-10-10    45
        2019-11-20    29
        2019-11-21    39
        2019-12-30    24
        2020-02-26    24
        2020-03-31    54
        2020-04-01   120
        2020-04-04    48
    '''

    like_df = pd.DataFrame(data['좋아요수'])
    unique_list = like_df['좋아요수'].unique()
    value = like_df['좋아요수'].value_counts()
    like_df_count = like_df['좋아요수'].value_counts().rename_axis('좋아요수목록').reset_index(name='빈도')
    like_df_count = like_df_count.sort_values(by=['좋아요수목록'], ascending = True).reset_index()

    plt.figure(figsize=(15,8))
    plt.xlabel('좋아요수목록')
    plt.ylabel('빈도')
    plt.title('좋아요수목록 별 빈도',fontsize=15)
    plt.scatter(like_df_count['좋아요수목록'],like_df_count['빈도'],label='빈도')
    plt.grid()
    plt.draw()
    fig = plt.gcf()
    fig.savefig(join(img_save_root,'좋아요수.png'),dpi=fig.dpi)

    '''
    대부분의 좋아요는 0, 좋아요가 0 인것을 제외하고 그래프를 생성했지만 특별히 다른점이 나타지 않음.    like_df_count = like_df_count.drop(index=0)
    좋아요수가 100이상의 좋아요를 받은목록은 아래와 같다.
    
    구분  진행상황        생성날짜                   ID  좋아요수                                                 제목                                                 내용
    229   보건의료   숙성중  2020-04-26  kakao20200413182156   122        트럼프의 ‘살균제 주입 치료’ 충격 발언에 대해 임상조사 검토를 요청 합니다.  ['위사진은 어느분 SNS 캡쳐 사진.https://news.naver.com/ma...
    393   사회복지   숙성중  2020-03-31  naver20200331202522   119                              [코로나 19 이후 민생회복 아이디어]  ['', '돌봄을 지자체로 이관시켜주세요돌봄 지자체 이관시 장점에 
    대하여 말씀드립니...
    401   사회복지   숙성중  2020-03-31  naver20200331202522   119                              [코로나 19 이후 민생회복 아이디어]  ['', '돌봄을 지자체로 이관시켜주세요돌봄 지자체 이관시 장점에 
    대하여 말씀드립니...
    834   보건의료  숙성종료  2019-12-27                  난다율   757            [2020정부혁신제안이벤트응모] 난임부부들의 「임신을 위한 지원 확대」  ['▶제안이유‘17년 10월부터 건강보험을 적용된
    난임치료 시술은, 도입한지 2년 ...
    865   보건의료  숙성종료  2019-12-18                  난다율   163                              난임부부들의 「임신을 위한 지원 확대」  ['▶제안이유‘17년 10월부터 건강보험을 적용된 난임치료  
    시술은, 도입한지 2년 ...
    1439    기타   숙성중  2019-03-18                 사필귀정   134  개인회생 변제기간 단축을 서울만 시행하고 지방은 차별하여 시행하지 않는 법이 어디있...  ['▶제안이유', "▶제안내용정성호 의원이
    발의, 변제기간 3년 단축을 적용한 「채...
    1447    기타   숙성중  2019-03-18                 사필귀정   134  개인회생 변제기간 단축을 서울만 시행하고 지방은 차별하여 시행하지 않는 법이 어디있...  ['▶제안이유', "▶제안내용정성호 의원이
    발의, 변제기간 3년 단축을 적용한 「채...
    1448    기타   숙성중  2019-03-17                  소확행   164                                     개인회생 기간단축 소급적용  ['▶제안이유', '▶제안내용대한민국 헌법이 전국 국민에게 해당되듯
    이,개인회생 기간...
    1612    기타   숙성중  2019-01-31                  NaN   103                                       개인회생단축소급지역차별  ['▶제안이유', '▶제안내용개인회생 단축소급 적용이 왜 법원마다 다른
    지 당최 이해...
    '''

    text_df = pd.DataFrame(data['내용'])
    text_data = str(np.array(text_df['내용'].tolist()))
    stop = set()
    stop.update(['인','해','또한','이','내','다른','등','위','가장','다시','도','것'])
    okt = Okt()
    text_data = okt.nouns(text_data)
    text_data = [each_word for each_word in text_data if each_word not in stop]
    text_data = nltk.Text(text_data)
    text_data = text_data.vocab().most_common(1000)

    print(text_data)
    text_data = dict(text_data)

    # img_path = r'C:\Users\82104\Documents\GitHub\Gwanghwamun_Suggestion\setting\korea.png'
    # font_path = r'C:\Users\82104\Documents\GitHub\Gwanghwamun_Suggestion\setting\NanumSquareRoundL.ttf'
    img_path = r'C:\ProgramData\Anaconda3\kdj\Git\Gwanghwamun_Suggestion\setting\korea.png'
    font_path = r'C:\ProgramData\Anaconda3\kdj\Git\Gwanghwamun_Suggestion\setting\NanumSquareRoundL.ttf'

    kore_mask = np.array(Image.open(img_path))
    word = WordCloud(min_font_size=30,max_font_size=300,
            font_path=font_path,background_color=(255,255,255),mask=kore_mask).generate_from_frequencies(text_data)

    plt.figure(figsize=(10,10))
    plt.axis('off')
    plt.margins(x=0,y=0)
    plt.imshow(word,interpolation="bilinear")
    plt.draw()
    fig = plt.gcf()
#     fig.savefig(join(img_save_root,'all_word_cloud.png'),dpi=fig.dpi)


    division_word_cloud = join(img_save_root,'division_word_cloud')
    os.makedirs(division_word_cloud,exist_ok=True)

    division_text_df = pd.DataFrame(data[['구분','내용']])
    for_division_list = division_text_df['구분'].unique()
    for x in for_division_list:
        text_df = division_text_df[division_text_df['구분'] == x]
        text_df = text_df.iloc[:,1:]
        text_data = str(np.array(text_df['내용'].tolist()))
        stop = set()
        stop.update(['인','것','등','이','시','제안','내용','수','각','더','및','회'])
        okt = Okt()
        text_data = okt.nouns(text_data)
        text_data = [each_word for each_word in text_data if each_word not in stop]
        text_data = nltk.Text(text_data)
        text_data = text_data.vocab().most_common(1000)

        print(text_data)
        text_data = dict(text_data)

        word = WordCloud(min_font_size=1,max_font_size=100,
                font_path=font_path,background_color=(255,255,255)).generate_from_frequencies(text_data)

        plt.figure(figsize=(10,10))
        plt.title(x,fontsize=30)
        plt.axis('off')
        plt.margins(x=0,y=0)
        plt.imshow(word,interpolation="bilinear")
        plt.draw()
        fig = plt.gcf()
        fig.savefig(join(division_word_cloud,x+'_word_cloud.png'),dpi=fig.dpi)


    date_text_df = pd.DataFrame(data[['생성날짜','내용']])
    for_date_list = ['2018-10-30',
                '2019-03-04',
                '2019-03-05',
                '2019-04-30',
                '2019-10-10',
                '2019-11-20',
                '2019-11-21',
                '2019-12-30',
                '2020-02-26',
                '2020-03-31',
                '2020-04-01',
                '2020-04-04']
    date_word_cloud = join(img_save_root,'date_word_cloud')
    os.makedirs(date_word_cloud,exist_ok=True)

    for x in for_date_list:
        text_df = date_text_df[date_text_df['생성날짜'] == x]
        text_df = text_df.iloc[:,1:]
        text_data = str(np.array(text_df['내용'].tolist()))
        stop = set()
        stop.update(['인','이','수','위','함','및','등','것','시','제안','내용','각','더'])
        okt = Okt()
        text_data = okt.nouns(text_data)
        text_data = [each_word for each_word in text_data if each_word not in stop]
        text_data = nltk.Text(text_data)
        text_data = text_data.vocab().most_common(1000)

        print(text_data)
        text_data = dict(text_data)

        word = WordCloud(min_font_size=1,max_font_size=100,
                font_path=font_path,background_color=(255,255,255)).generate_from_frequencies(text_data)

        plt.figure(figsize=(10,10))
        plt.title(x,fontsize=30)
        plt.axis('off')
        plt.margins(x=0,y=0)
        plt.imshow(word,interpolation="bilinear")
        plt.draw()
        fig = plt.gcf()
        fig.savefig(join(date_word_cloud,x+'_word_cloud.png'),dpi=fig.dpi)