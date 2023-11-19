import json

MovieFile = "movies.json"

def load_movies():
    try:
        with open(MovieFile, "r") as file:
            movies = json.load(file)
    except FileNotFoundError:
        movies = []
    return movies

def save_movies(movies):
    with open(MovieFile, "w") as file:
        json.dump(movies, file, indent=2)

def list_of_all_movies():
    movies = load_movies()
    if not movies:
        print("No movies found.")
    else:
        for movie in movies:
            print_movie_details(movie)

def print_movie_details(movie):
    print(f"Title: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release Year: {movie['release_year']}")
    print(f"Language: {movie['language']}")
    print(f"Rating: {movie['rating']}")
    print("-" * 20)

def add_new_movie():
    movies = load_movies()
    name = input("Enter movie name: ")
    director = input("Enter director's name: ")
    release_year = int(input("Enter release year: "))
    language = input("Enter language: ")
    rating = float(input("Enter rating(1-10): "))

    new_movie = {
        "name": name,
        "director": director,
        "release_year": release_year,
        "language": language,
        "rating": rating
    }

    movies.append(new_movie)
    save_movies(movies)
    print("Movie added successfully.")

def filter_movies():
    movies = load_movies()

    print("Filter Options:")
    print("1. Filter by Name")
    print("2. Filter by Director")
    print("3. Filter by Release Year")
    print("4. Filter by Language")
    print("5. Filter by Rating")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        filter_value = input("Enter movie name to filter: ")
        filtered_movies = [movie for movie in movies if filter_value.lower() in movie["name"].lower()]
    elif choice == 2:
        filter_value = input("Enter director's name to filter: ")
        filtered_movies = [movie for movie in movies if filter_value.lower() in movie["director"].lower()]
    elif choice == 3:
        filter_value = int(input("Enter release year to filter: "))
        filtered_movies = [movie for movie in movies if filter_value == movie["release_year"]]
    elif choice == 4:
        filter_value = input("Enter language to filter: ")
        filtered_movies = [movie for movie in movies if filter_value.lower() in movie["language"].lower()]
    elif choice == 5:
        filter_value = float(input("Enter rating to filter: "))
        filtered_movies = [movie for movie in movies if filter_value == movie["rating"]]
    else:
        print("Invalid choice.")
        return

    if not filtered_movies:
        print("No movies found.")
    else:
        for movie in filtered_movies:
            print_movie_details(movie)

def search_movie():
    movies = load_movies()
    search_term = input("Enter the movie name to search: ")
    search_results = [movie for movie in movies if search_term.lower() in movie["name"].lower()]

    if not search_results:
        print("No matching movies found.")
    else:
        for movie in search_results:
            print_movie_details(movie)

def update_movie():
    movies = load_movies()
    search_term = input("Enter the movie name to update: ")
    movie_to_update = next((movie for movie in movies if search_term.lower() in movie["name"].lower()), None)

    if movie_to_update:
        print("Current Movie Details:")
        print_movie_details(movie_to_update)

        movie_to_update["name"] = input("Enter new movie name: ")
        movie_to_update["director"] = input("Enter new director's name: ")
        movie_to_update["release_year"] = int(input("Enter new release year: "))
        movie_to_update["language"] = input("Enter new language: ")
        movie_to_update["rating"] = float(input("Enter new rating: "))

        save_movies(movies)
        print("Movie updated successfully.")
    else:
        print("Movie not found.")

def delete_movie():
    movies = load_movies()
    search_term = input("Enter the movie name to delete: ")
    movie_to_delete = next((movie for movie in movies if search_term.lower() in movie["name"].lower()), None)

    if movie_to_delete:
        print("Movie to be deleted:")
        print_movie_details(movie_to_delete)

        confirmation = input("Are you sure you want to delete this movie? (yes/no): ").lower()
        if confirmation == "yes":
            movies.remove(movie_to_delete)
            save_movies(movies)
            print("Movie deleted successfully.")
        else:
            print("Deletion canceled.")
    else:
        print("Movie not found.")

def get_number_of_movies_by_language():
    movies = load_movies()
    language_counts = {}

    for movie in movies:
        language = movie["language"]
        language_counts[language] = language_counts.get(language, 0) + 1

    for language, count in language_counts.items():
        print(f"{language}: {count} movies")

# Main Menu
while True:
    print("\nMovie List Application")
    print("1. list of all movies")
    print("2. Add a New Movie")
    print("3. Filter Movies")
    print("4. Search for a Movie")
    print("5. Update a Movie's Details")
    print("6. Delete a Movie")
    print("7. Get Number of Movies by Language")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        list_of_all_movies()
    elif choice == "2":
        add_new_movie()
    elif choice == "3":
        filter_movies()
    elif choice == "4":
        search_movie()
    elif choice == "5":
        update_movie()
    elif choice == "6":
        delete_movie()
    elif choice == "7":
        get_number_of_movies_by_language()
    elif choice == "8":
        print(" Have a Happy Day! Do visit again.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")