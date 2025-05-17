import streamlit as st
import pickle
import pandas as pd
import requests

API_KEY = "ce7537b372fba40bdc5e5b8ba60a143b"

def fetch_poster(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={"ce7537b372fba40bdc5e5b8ba60a143b"}&query={title}"
    response = requests.get(url)
    data = response.json()
    
    if data['results']:
        poster_path = data['results'][0]['poster_path']
        full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
        return full_path
    else:
        return "https://via.placeholder.com/300x450?text=No+Image"

def recommend(movie):
    matches = movies[movies["title"] == movie]
    if matches.empty:
        return [], []
    
    movie_index = matches.index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:11]
    
    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_title = movies.iloc[i[0]].title
        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_poster(movie_title))
    
    return recommended_movies, recommended_posters


movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("🎬 Movie Recommendation System")

selected_movie_name = st.selectbox("Hello! Welcome to the system. Select your preferred movie:", movies["title"].values)

if st.button("Recommend"):
    movie_names, movie_posters = recommend(selected_movie_name)
    
    for i in range(0, len(movie_names), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(movie_names):
                with cols[j]:
                    st.image(movie_posters[i + j], caption=movie_names[i + j],  use_container_width=True)
