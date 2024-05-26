import streamlit as st
import random

# Dictionary of movies categorized by genre
movies = {
    "action": ["The Dark Knight", "Inception", "Mad Max: Fury Road", "Die Hard"],
    "comedy": ["The Hangover", "Superbad", "Dumb and Dumber", "Anchorman"],
    "drama": ["The Shawshank Redemption", "The Godfather", "Forrest Gump", "Schindler's List"],
    "horror": ["The Shining", "Get Out", "A Quiet Place", "The Conjuring"]
}

# Function to recommend a movie based on genre
def recommend_movie(genre):
    if genre.lower() in movies:
        return random.choice(movies[genre.lower()])
    else:
        return "Sorry, we don't have recommendations for that genre."

# Main function to run the Streamlit app
def main():
    st.title("Movie Recommender")
    st.subheader("Welcome to Movie Recommender! Get personalized movie recommendations based on your preferred genre.")

    # Ask user for their preferred genre
    genre = st.selectbox("Select your preferred movie genre:", ["Action", "Comedy", "Drama", "Horror"])

    # Recommend a movie based on the user's preference
    if st.button("Recommend"):
        recommendation = recommend_movie(genre)
        st.success(f"We recommend you watch: {recommendation}")

if __name__ == "__main__":
    main()
