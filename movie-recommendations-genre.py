import streamlit as st
import openai
import random

# Dictionary of movies categorized by genre
movies = {
    "action": ["Atlas", "The Fall Guy", "Mad Max: Fury Road", "Die Hard"],
    "comedy": ["Legally Blonde", "White Chicks", "Matilda", "Family Switch"],
    "drama": ["Little Women", "20th Century Girl", "Purple Hearts", "Five Feet Apart"],
    "horror": ["The Medium", "Gonjiam:Haunted Asylum", "A Quiet Place", "The Conjuring"]
}

# Function to recommend a movie based on genre
def recommend_movie(genre):
    if genre.lower() in movies:
        return random.choice(movies[genre.lower()])
    else:
        return "Sorry, we don't have recommendations for that genre."

# Main function to run the Streamlit app
def main():
    st.title("CineMatch")
    st.subheader("Welcome to CineMatch:Your Personal Movie Companion! Get personalized movie recommendations based on your preferred genre.")

    # Ask user for their preferred genre
    genre = st.selectbox("Select your preferred movie genre:", ["Action", "Comedy", "Drama", "Horror"])

    # Recommend a movie based on the user's preference
    if st.button("Recommend"):
        recommendation = recommend_movie(genre)
        st.success(f"We recommend you watch: {recommendation}")

if __name__ == "__main__":
    main()
