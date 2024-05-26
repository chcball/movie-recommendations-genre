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

# Main function
def main():
    print("Welcome to the Movie Recommender!")

    # Ask user for their preferred genre
    genre = input("Please enter your preferred genre (action, comedy, drama, horror): ")

    # Recommend a movie based on the user's preference
    recommendation = recommend_movie(genre)
    print("We recommend you watch:", recommendation)

if __name__ == "__main__":
    main()
