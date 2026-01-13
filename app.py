import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load MovieLens 100k movie data
columns = ['movieId', 'title', 'release_date', 'video_release_date', 'IMDb_URL',
           'unknown', 'Action', 'Adventure', 'Animation', "Children's", 'Comedy',
           'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror',
           'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

movies = pd.read_csv('u.item', sep='|', names=columns, encoding='latin-1')

# Combine genre columns into a single string
genre_cols = columns[5:]
movies['genres'] = movies[genre_cols].apply(
    lambda x: ' '.join([genre for genre in genre_cols if x[genre] == 1]), axis=1
)

movies = movies[['movieId', 'title', 'genres']]

# Create TF-IDF matrix for genres
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

# Compute cosine similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Helper function to get recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Top 10 similar movies
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()

# Streamlit UI
st.title("🎬 Movie Recommendation System")
selected_movie = st.selectbox("Select a movie you like:", movies['title'].values)

if st.button("Show Recommendations"):
    recommendations = get_recommendations(selected_movie)
    st.subheader("Recommended Movies:")
    for i, rec in enumerate(recommendations, 1):
        st.write(f"{i}. {rec}")

