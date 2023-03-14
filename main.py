
import pandas as pd
from sklearn.metrics.pairwise import cosine_distances
from sklearn.feature_extraction.text import CountVectorizer


df = pd.read_csv('E:/web development/flask/last.csv')
df.drop(columns=['Unnamed: 0'], inplace=True)


cv = CountVectorizer().fit_transform(df['feature_extraction'])

cs = cosine_distances(cv)


def get_movie(data):
    mov_id = df[df.original_title == data]['Movie_id'].values[0]
    score = list(enumerate(cs[mov_id]))
    sort_score = sorted(score, key=lambda x: x[1], reverse=False)
    sort_score = sort_score[1:]
    name_recom = []
    d=0
    for item in sort_score:
        name_recom.append(df[df.Movie_id==item[0]]['original_title'].values[0])
        d+=1
        if d==5:
            break
    return name_recom
    
        