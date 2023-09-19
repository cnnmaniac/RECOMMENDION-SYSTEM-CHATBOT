import random
import tkinter as tk
from tkinter import scrolledtext

# Define a dictionary of movies and their associated genres.
movies = {
    "Shridi Sai Baba": ["action", "adventure", "science fiction", "saibaba" ],
    "Movie 2": ["comedy", "romance"],
    "Movie 3": ["drama", "romance"],
    "Movie 4": ["action", "adventure", "fantasy"],
    "Movie 5": ["horror", "thriller"],
}

# Define a function to recommend a movie based on a given genre.
def recommend_movie(genre):
    genre = genre.lower()
    recommended_movies = []

    for movie, genres in movies.items():
        if genre in genres:
            recommended_movies.append(movie)

    if recommended_movies:
        return random.choice(recommended_movies)
    else:
        return "I couldn't find any movies in that genre. Please try another genre."

# Define a function to handle button click event.
def recommend_movie_button_click():
    user_genre = genre_entry.get().strip()
    recommended_movie = recommend_movie(user_genre)

    # Clear previous output and display the new recommendation.
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"Recommended movie in the {user_genre} genre: {recommended_movie}\n")
    output_text.config(state=tk.DISABLED)

# Create the main application window.
app = tk.Tk()
app.title("Movie Recommendation App")

# Create and configure the genre input entry widget.
genre_label = tk.Label(app, text="Enter Genre:")
genre_label.pack()
genre_entry = tk.Entry(app)
genre_entry.pack()

# Create the recommend button.
recommend_button = tk.Button(app, text="Recommend Movie", command=recommend_movie_button_click)
recommend_button.pack()

# Create and configure the output text widget.
output_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, height=5, state=tk.DISABLED)
output_text.pack()

# Start the main application loop.
app.mainloop()
