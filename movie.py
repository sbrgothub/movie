import streamlit as st
import gzip
import pickle
from sklearn.metrics.pairwise import cosine_similarity
with gzip.open("movie.pkl.gz", "rb") as obj:
    data = pickle.load(obj)
movie_dictionary=data['movie_dict']

def recomend(movie,n=6):
  if movie in movie_dictionary:
    v_in=movie_dictionary[movie]
    cosine_dit={}
    for i,v_check in movie_dictionary.items():
      if i!=movie:
        cosine_dit[i]=cosine_similarity(v_in,v_check)[0][0]
    result=sorted(cosine_dit.items(),key=lambda a:a[1],reverse=True)
    return [i[0] for i in result[:n]]
  else:
    return "not available"

st.title('Movie recommendation App 🎥')
movie=st.selectbox('select a movie',movie_dictionary.keys())
button=st.button('Recomend')

if button:
  found=recomend(movie,n=6)
  for i in found:
    st.write(i)
    df=data['df']
    for k in ['Genre','Poster_Link','Overview']:
      if k=='Poster_Link':
        st.image(df.loc[df['Series_Title']==i,k].iloc[0])
      else:
        st.write(df.loc[df['Series_Title']==i,k].iloc[0])
      st.write('___'*60)
