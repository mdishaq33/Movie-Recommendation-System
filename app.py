from flask import Flask, render_template, request
import pickle
import pandas as pd
import requests

app = Flask(__name__)

# Load your model and data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarirty.pkl', 'rb'))

# Function to fetch movie poster
def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=d8d4ae807066757910fae91d5193629e&language=en-US'
    response = requests.get(url)
    data = response.json()
    if 'poster_path' in data and data['poster_path']:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        return "https://via.placeholder.com/500x750?text=No+Poster"

# Function to recommend movies based on selected movie
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

# Home route
@app.route('/')
def home():
    return render_template('index.html', movies=list(movies['title'].values))

# Route for recommendations
@app.route('/recommend', methods=['POST'])
def recommend_movies():
    selected_movie = request.form['movie']
    names, posters = recommend(selected_movie)
    return render_template('recommend.html', movies=zip(names, posters))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
