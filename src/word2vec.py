from lib import os,glob,sys
from lib import join,basename,dirname
from lib import pd,np,re,plt,fm,openpyxl
from lib import Okt
from lib import word2vec
from lib import DBSCAN

def make_vec_model(data,save_root,data_name : str):
    okt = Okt()
    result = []
    for line in data:
        malist = okt.pos(line, norm=True, stem=True)
        r = []
        for word in malist:
            if not word[1] in ['Josa','Eomi','Punctuation']:
                r.append(word[0])
        rl = (' '.join(r))
        result.append(rl)
    
    data_save_path = join(save_root,data_name + '.nlp')
    with open(data_save_path,'w',encoding='utf-8') as f:
        f.write("\n".join(result))
    
    wData = word2vec.LineSentence(data_save_path)
    wModel =word2vec.Word2Vec(wData, size=100, window=10, hs=1, min_count=2, sg=1)
    wModel.save(data_save_path+'.model')
    model = word2vec.Word2Vec.load(data_save_path+'.model')
    return model

def cluster(eps,min_sample_size,model,save_path):
    model = model
    word_vector = model.wv.vectors
    match_index = model.wv.index2word
    model.init_sims(replace=True)
    han = re.compile(r'[가-힣]{2,}')
    dbscan = DBSCAN(eps=eps,min_samples=min_sample_size)
    cluster = dbscan.fit_predict(word_vector)

    df = pd.DataFrame(cluster,columns=['cluster'],index=match_index).reset_index()
    df.columns = ['word','cluster']
    df = df[df['word'].apply(lambda x: len(han.findall(x)) > 0)]
    df = df[df['cluster'] != -1]
    print(df.groupby(['cluster']).count())
    df.to_excel(pd.ExcelWriter(save_path + 'cluster.xlsx'),index=False)
    excel_path = save_path + 'cluster.xlsx'
    return excel_path

def plot(excel_path,font_path):
    clstr = pd.read_excel(pd.ExcelFile(excel_path))
    min_cluster = clstr["cluster"].min()
    max_cluster = clstr["cluster"].max()

    print(min_cluster, max_cluster)
    for clstr_num in range(min_cluster, max_cluster + 1):
        clstr_index = clstr[clstr["cluster"] == clstr_num].index
        clstr.loc[clstr_index, "value"] = list(range(0, len(clstr_index) * 3, 3))

    font = fm.FontProperties(fname=font_path, size=12)

    fig, ax = plt.subplots()
    clstr.plot.scatter(x="cluster", y="value", ax=ax)
    clstr[["cluster", "value", "word"]].apply(lambda x: ax.text(*x, fontproperties=font), axis=1)
    plt.show()


if __name__ == '__main__':
    root = r'C:\Users\82104\Documents\GitHub\Gwanghwamun_Suggestion\data'
    font_path = r'C:\Users\82104\Documents\GitHub\Gwanghwamun_Suggestion\setting\NanumSquareRoundL.ttf'
    save_root = join(dirname(root),'src','word2vec')
    os.makedirs(save_root,exist_ok=True)

    data_path = glob.glob(join(root,'*.txt'))[-1]
    data = pd.read_csv(data_path,sep='\t',header=None,encoding='utf8')
    data.columns = ['구분','진행상황','생성날짜','ID','좋아요수','제목','내용']

    text_data = data['내용']
    title = list(text_data)

    model = make_vec_model(title,save_root,'title')
    excel_path = cluster(1,10,model,save_root)
    plot(excel_path,font_path)