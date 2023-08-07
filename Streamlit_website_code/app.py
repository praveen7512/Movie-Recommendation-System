import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:20]
    recommnended_movies=[]
    for i in movie_list:
        recommnended_movies.append(movies.iloc[i[0]].title)
    return recommnended_movies

movie_dict =pickle.load(open('movie_dict.pkl','rb'))
movies =pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System ')

selected_movie =st.selectbox(
    'Select the movie that you want to watch',
    movies['title'].values )

if st.button('Recommend'):
    recommend_movie_list=recommend(selected_movie)

    for i in recommend_movie_list:
        st.divider()
        with st.container():
          st.write(i)











