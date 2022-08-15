import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
	response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
	data=response.json()
	return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

movies_list=pickle.load(open("movies.pkl","rb"))
movies_title=movies_list["title"].values

similarity=pickle.load(open("similarity.pkl","rb"))

def recommend(movie):
    movie_index=movies_list[movies_list["title"]==movie].index[0]
    sim_index=similarity[movie_index]
    sort=list(sorted(enumerate(sim_index),reverse=True,key=lambda x:x[1]))
    first_five=sort[1:6]
    recommended=[]
    recommended_movies_id=[]
    for i in first_five:
    	movie_id=movies_list["id"].iloc[i[0]]
    	recommended.append(movies_list["title"].iloc[i[0]])
    	recommended_movies_id.append(movie_id)
    return recommended,recommended_movies_id

st.subheader("Movie recommendation Engine:popcorn:")
st.write("---")
st.write("")
with st.container():

    st.markdown("<h1 style='text-align: center; color: #C60000;'>MOVIE BUFF</h1>",unsafe_allow_html=True)
    st.write("")
    st.image("movie.jpg")
    st.write("---")
    st.write("")
    st.write("")
    st.write("Hi, I'm a movie recommendation engine, I work on the basis of ML-approach, if you are looking for someone who can suggest some movies related to the movies that you have already watched or going to watch, then I'm the one you are seeking for.")
    st.write("Movie will be recommended on the basis of the movies that you browsed below.")
st.write("")
st.write("")
selection=st.selectbox("BROWSE MOVIE",
	               (movies_title)
	               )


if st.button("SHOW"):
	names,ids=recommend(selection)
	st.write("Here are some movies related to your search")
	st.write()

	col1,col2,col3,col4,col5=st.columns(5)

	with col1:
		st.image(fetch_poster(ids[0]))
		st.write(names[0])

	with col2:
		st.image(fetch_poster(ids[1]))
		st.write(names[1])

	with col3:
		st.image(fetch_poster(ids[2]))
		st.write(names[2])
	with col4:
		st.image(fetch_poster(ids[3]))
		st.write(names[3])
	with col5:
		st.image(fetch_poster(ids[4]))
		st.write(names[4])
