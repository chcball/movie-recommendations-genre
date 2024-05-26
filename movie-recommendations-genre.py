import streamlit as st
import random
import google.generativeai as genai
from dotenv import load_dotenv

# Dictionary of movies categorized by genre with descriptions
movies_with_descriptions = {
    "action": [
        {"title": "Atlas", "description": "A team of explorers discover a hidden world within the Earth's core."},
        {"title": "The Fall Guy", "description": "A stuntman moonlights as a bounty hunter."},
        {"title": "Mad Max: Fury Road", "description": "In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler in search of her homeland."},
        {"title": "Die Hard", "description": "An NYPD officer tries to save his wife and several others taken hostage by German terrorists during a Christmas party at the Nakatomi Plaza in Los Angeles."}
    ],
    "comedy": [
        {"title": "Legally Blonde", "description": "A blonde sorority queen enrolls in Harvard Law School to win back her ex-boyfriend."},
        {"title": "White Chicks", "description": "Two disgraced FBI agents go undercover as high society debutantes to thwart a kidnapping plot."},
        {"title": "Matilda", "description": "A young genius girl with psychokinetic abilities is mistreated by her parents and headmistress."},
        {"title": "Family Switch", "description": "Two families from different social classes accidentally switch babies at the hospital."}
    ],
    "drama": [
        {"title": "Little Women", "description": "Four sisters come of age in America in the aftermath of the Civil War."},
        {"title": "20th Century Girl", "description": "A young girl comes of age in California during the 1970s."},
        {"title": "Purple Hearts", "description": "The story of a Navy nurse and her experiences during the Vietnam War."},
        {"title": "Five Feet Apart", "description": "Two teenagers with cystic fibrosis fall in love but are forced to stay apart to avoid risking their lives."}
    ],
    "horror": [
        {"title": "The Medium", "description": "A documentary filmmaker explores a haunted house and encounters supernatural entities."},
        {"title": "Gonjiam: Haunted Asylum", "description": "A group of people explore an abandoned asylum and encounter terrifying paranormal activities."},
        {"title": "A Quiet Place", "description": "In a post-apocalyptic world, a family must live in silence to avoid being hunted by mysterious creatures."},
        {"title": "The Conjuring", "description": "Paranormal investigators help a family haunted by a dark presence in their farmhouse."}
    ]
}

# Function to recommend a movie based on genre
def recommend_movie(genre):
    if genre.lower() in movies_with_descriptions:
        return random.choice(movies_with_descriptions[genre.lower()])
    else:
        return "Sorry, we don't have recommendations for that genre."

# Main function to run the Streamlit app
def main():
    st.title("CineMatch")
    st.subheader("Welcome to CineMatch: Your Personal Movie Companion! Get personalized movie recommendations based on your preferred genre.")

    # Ask user for their preferred genre
    genre = st.selectbox("Select your preferred movie genre:", ["Action", "Comedy", "Drama", "Horror"])

    # Recommend a movie based on the user's preference
    if st.button("Recommend"):
        recommendation = recommend_movie(genre)
        st.success(f"We recommend you watch: {recommendation['title']} - {recommendation['description']}")

if __name__ == "__main__":
    main()
