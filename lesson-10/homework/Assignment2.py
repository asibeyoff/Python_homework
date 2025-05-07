import requests
import random

def get_genre_id(genre_name, api_key):
    genre_url = "https://api.themoviedb.org/3/genre/movie/list"
    response = requests.get(genre_url, params={"api_key": api_key})
    genres = response.json()["genres"]
    for genre in genres:
        if genre["name"].lower() == genre_name.lower():
            return genre["id"]
    return None

def recommend_movie(genre_name):
    API_KEY = 'YOUR_API_KEY'  # Replace with your TMDb API key

    genre_id = get_genre_id(genre_name, API_KEY)
    if not genre_id:
        print("Genre not found.")
        return

    discover_url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": API_KEY,
        "with_genres": genre_id,
        "sort_by": "popularity.desc",
        "page": random.randint(1, 5)
    }

    response = requests.get(discover_url, params=params)
    movies = response.json().get("results", [])

    if movies:
        movie = random.choice(movies)
        print(f"\n🎬 Movie Recommendation in '{genre_name.title()}':")
        print(f"Title: {movie['title']}")
        print(f"Overview: {movie['overview']}")
    else:
        print("No movies found for that genre.")

# Example usage
genre_input = input("Enter a movie genre (e.g., Action, Comedy, Drama): ")
recommend_movie(genre_input)

