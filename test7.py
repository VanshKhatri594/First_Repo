movie_ratings = {
    "Inception": 8.8,
    "Interstellar": 8.6,
    "Parasite": 8.9,
    "The Dark Knight": 9.0,
    "Avengers: Endgame": 8.4
}

# Expected Output:
# Highest Rated Movie: The Dark Knight (9.0)
# Top 3 Movies: [('The Dark Knight', 9.0), ('Parasite', 8.9), ('Inception', 8.8)]
# Average Rating: 8.74

def analyze_movie_ratings(movie_ratings):
    highest_rated = max(movie_ratings, key=movie_ratings.get)
    highest_rating = movie_ratings[highest_rated]

    top_movies = sorted(movie_ratings.items(), key=lambda x: x[1], reverse=True)[:3]

    avg_rating = sum(movie_ratings.values()) / len(movie_ratings)

    print(f"Highest Rated Movie: {highest_rated} ({highest_rating})")
    print(f"Top 3 Movies: {top_movies}")
    print(f"Average Rating: {avg_rating}")

analyze_movie_ratings(movie_ratings)
