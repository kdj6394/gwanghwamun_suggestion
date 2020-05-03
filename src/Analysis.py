from lib import os,glob,sys,join,basename,dirname
from lib import np,pd,plt,sns
plt.rc('font',family='Malgun Gothic')


if __name__ == '__main__':
    root = r'C:\Users\82104\Documents\GitHub\Gwanghwamun_Suggestion\data'
    img_save_root = join(dirname(root),'src','Analysis_img')
    os.makedirs(img_save_root,exist_ok=True)

    data_path = glob.glob(join(root,'*.txt'))[-1]
    data = pd.read_csv(data_path,sep='\t',header=None)
    
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
    -> 위의 결과로 word Cloud 를 생성시 범위를 나눠 그릴 예정 ex) [기타],[청원횟수100~200],[청원횟수0~100]
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
    plt.grid()
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