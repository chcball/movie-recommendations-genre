import streamlit as st
import random
import google.generativeai as genai
from dotenv import load_dotenv

# Dictionary of movies categorized by genre with descriptions
movies_with_descriptions = {
    "action": [
        {"title": "Atlas", "description": "A team of explorers discover a hidden world within the Earth's core. A bleak-sounding future, where an AI soldier has determined that the only way to end the war is to end humanity."},
        {"title": "The Fall Guy", "description": "He's a stuntman, and like everyone in the stunt community, he gets blown up, shot, crashed, thrown through windows, and dropped from the highest of heights, all for our entertainment. And now, fresh off an almost career-ending accident, this working-class hero has to track down a missing movie star, solve a conspiracy, and try to win back the love of his life while still doing his day job. What could possibly go right?"},
        {"title": "Mad Max: Fury Road", "description": "In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler in search of her homeland with the aid of a group of female prisoners, a psychotic worshiper, and a drifter named Max."},
        {"title": "Die Hard", "description": "An NYPD officer tries to save his wife and several others taken hostage by German terrorists during a Christmas party at the Nakatomi Plaza in Los Angeles."}
    ],
    "comedy": [
        {"title": "Legally Blonde", "description": "Elle Woods, a blonde, fashionable sorority queen is dumped by her boyfriend. She decides to follow him to law school. While she is there, she figures out that there is more to her than just looks."},
        {"title": "White Chicks", "description": "After an unsuccessful mission, FBI agents Kevin and Marcus Copeland fall into disgrace at the agency. They decide to work undercover on an abduction case disguised as Brittany and Tiffany Wilson, the vain, spoiled white daughters of a tycoon."},
        {"title": "Matilda", "description": "A young genius girl with psychokinetic abilities is mistreated by her parents and headmistress."},
        {"title": "Family Switch", "description": "When a chance encounter with an astrological reader causes the Walkers to wake up to a full body switch, can they unite to land a promotion, college interview, record deal, and soccer tryout?."}
    ],
    "drama": [
        {"title": "Little Women", "description": "In the years after the Civil War, Jo March lives in New York and makes her living as a writer, while her sister Amy studies painting in Paris. Amy has a chance encounter with Theodore, a childhood crush who proposed to Jo but was ultimately rejected. Their oldest sibling, Meg, is married to a schoolteacher, while shy sister Beth develops a devastating illness that brings the family back together.."},
        {"title": "20th Century Girl", "description": "A teen girl has her eyes set on a boy for her lovesick best friend. However, things become complicated when she falls in love and is forced to choose between love and friendship.."},
        {"title": "Purple Hearts", "description": "Cassie, a struggling singer-songwriter agrees to marry a troubled Marine, Luke for military benefits. The line between real and pretend begins to blur.."},
        {"title": "Five Feet Apart", "description": "Cystic fibrosis patient, Stella, navigates routines and limitations in the hospital. A spark with charming Will, another patient with the same illness, challenges her self-control. As their connection deepens, defying the safe-distance rule becomes a tempting gamble.."}
    ],
    "horror": [
        {"title": "The Medium", "description": "In the Isan region of Thailand, a shaman realizes that his nephew has been possessed. However, the goddess that appears to have taken possession turns out not to be as benevolent as she first appears.."},
        {"title": "Gonjiam: Haunted Asylum", "description": "The crew of a horror web series travels to an abandoned asylum for a live broadcast. It soon encounters much more than expected as it moves deeper inside the nightmarish old building.."},
        {"title": "A Quiet Place", "description": "If they hear you, they hunt you. A family must live in silence to avoid mysterious creatures that hunt by sound. Knowing that even the slightest whisper or footstep can bring death, Evelyn and Lee are determined to find a way to protect their children while desperately searching for a way to fight back.."},
        {"title": "The Conjuring", "description": "1970s paranormal investigators Ed & Lorraine Warren (Wilson & Farmiga) tackle a farmhouse haunting for the Perron family (Taylor & Livingston). The initial benign presence turns terrifying as the Warrens unearth the house's dark history.."}
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
