# Given a dictionary where movie names are keys and their respective ratings (out of 10) are values, determine:
#
# The highest-rated movie.
# The top 3 movies sorted by rating.
# The average movie rating

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

highest_rated = max(movie_ratings,key=movie_ratings.get)
print(f"Highest Rated Movie: {highest_rated}")

top_movies = sorted(movie_ratings.items(), key=lambda x : x[1], reverse=True)
print(f"Top 3 Movies : {top_movies[:3]}")

total = sum(movie_ratings.values())

avg = total / len(movie_ratings)
print(f"Average Rating : {avg}")
