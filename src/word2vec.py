from lib import os,glob,sys,tqdm
from lib import join,basename,dirname
from lib import pd,np,re,plt,fm,openpyxl
from lib import warnings
warnings.filterwarnings(action='ignore')
from lib import Okt,word2vec,DBSCAN,KMeans
from lib import TSNE,matplotlib

def make_vec_model(data,save_root,data_name : str,min_cnt : int):
    okt = Okt()
    result = []
    for line in tqdm(data):
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
    wModel =word2vec.Word2Vec(wData, size=100, window=5, workers=4 ,min_count=min_cnt, sg=1)
    wModel.save(data_save_path+'.model')
    model = word2vec.Word2Vec.load(data_save_path+'.model')
    return model

def kmeans_clustering(model,div_int:int):
    word_vectors = model.wv.syn0
    num_clusters = int(word_vectors.shape[0]/div_int)
    print(num_clusters)
    num_clusters = int(num_clusters)

    kmeans_clustering = KMeans(n_clusters=num_clusters)
    idx = kmeans_clustering.fit_predict(word_vectors)
    idx = list(idx)

    names = model.wv.index2word
    word_centroid_map = {names[i]: idx[i] for i in range(len(names))}

    for c in range(num_clusters):
        print("\ncluster {}".format(c))
        words_list = list()
        cluster_values = list(word_centroid_map.values())
        for i in range(len(cluster_values)):
            if (cluster_values[i] == c):
                words_list.append(list(word_centroid_map.keys())[i])            
        print(words_list)

    vocab = list(model.wv.vocab)
    X = model[vocab]
    tsne = TSNE(n_components=2)
    X_tsne = tsne.fit_transform(X)
    df = pd.DataFrame(X_tsne, index=vocab, columns=["x", "y"])
    return df

def plot_scatter(df,font_path):
    prop = fm.FontProperties(fname=font_path)
    matplotlib.rcParams["axes.unicode_minus"] = False
    fig = plt.figure(figsize=(15,8))
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(df["x"], df["y"])
    for word, pos in list(df.iterrows()):
        ax.annotate(word, pos, fontsize=10,fontproperties=prop,textcoords='offset points')
    plt.show()

if __name__ == '__main__':
    root = r'C:\Users\82104\Documents\GitHub\Gwanghwamun_Suggestion\data'
    font_path = r'C:\Users\82104\Documents\GitHub\Gwanghwamun_Suggestion\setting\NanumSquareRoundL.ttf'
    # root = r'C:\ProgramData\Anaconda3\kdj\Git\Gwanghwamun_Suggestion\data'
    # font_path = r'C:\ProgramData\Anaconda3\kdj\Git\Gwanghwamun_Suggestion\setting\NanumSquareRoundL.ttf'

    save_root = join(dirname(root),'src','word2vec')
    os.makedirs(save_root,exist_ok=True)

    data_path = glob.glob(join(root,'*.txt'))[-1]
    data = pd.read_csv(data_path,sep='\t',header=None,encoding='utf8')
    data.columns = ['구분','진행상황','생성날짜','ID','좋아요수','제목','내용']

    text_data = data['제목']
    title = list(text_data)

    model = make_vec_model(title,save_root,'title',14)
    df = kmeans_clustering(model,30)
    plot_scatter(df,font_path)