from TMDB_API import get_genres, search_movies
import json
import os

WATCHLIST_FILE = "watchlist.json"

def load_watchlist(filepath=WATCHLIST_FILE):
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    return []

def save_watchlist(watchlist, filepath=WATCHLIST_FILE):
    with open(filepath, "w") as f:
        json.dump(watchlist, f, indent=2)

def display_movies(movies):
    if not movies:
        print("No movies found.")
        return
    print(f"\nShowing {len(movies)} Movie(s) Ordered by Rating:\n")
    for i, movie in enumerate(movies, 1):
        title = movie.get("title", "N/A")
        year = movie.get("release_date", "N/A")[:4]
        rating = movie.get("vote_average", "N/A")
        print(f"{i}. {title} ({year}) - ⭐ {rating}")

def view_watchlist_menu():
    while True:
        watchlist = load_watchlist()
        if not watchlist:
            print("\n📂 Your watchlist is empty.")
        else:
            print("\n📂 Your Watchlist:")
            for i, movie in enumerate(watchlist, 1):
                title = movie.get("title", "N/A")
                year = movie.get("release_date", "N/A")[:4]
                rating = movie.get("vote_average", "N/A")
                print(f"{i}. {title} ({year}) - ⭐ {rating}")

        print("\nOptions:")
        print("[a] Add movie from search")
        print("[r] Remove movie")
        print("[c] Clear watchlist")
        print("[q] Quit watchlist")
        choice = input("Enter choice: ").strip().lower()

        if choice == "a":
            return "add"
        elif choice == "r":
            index = input("Enter the number of the movie to remove: ").strip()
            if index.isdigit():
                idx = int(index) - 1
                if 0 <= idx < len(watchlist):
                    removed = watchlist.pop(idx)
                    save_watchlist(watchlist)
                    print(f"🗑️ Removed: {removed['title']}")
                else:
                    print("❌ Invalid number.")
        elif choice == "c":
            confirm = input("Are you sure you want to clear the watchlist? (y/n): ").strip().lower()
            if confirm == "y":
                save_watchlist([])
                print("✅ Watchlist cleared.")
        elif choice == "q":
            return "back"
        else:
            print("❌ Invalid choice.")

def main():
    print("🎬 Welcome to MovieMatch!")

    choice = input("Do you want to open your watchlist? (y/n): ").strip().lower()
    if choice == "y":
        view_watchlist_menu()

    genres = get_genres()
    print("\nAvailable genres:")
    for name in genres:
        print(f" - {name.title()}")

    user_genre = input("\nEnter a genre you like: ").strip().lower()
    genre_id = genres.get(user_genre)
    if not genre_id:
        print("❌ Genre not found.")
        return

    user_input = input("Enter release year (e.g. 2015) or decade (e.g. 1990s), or leave blank: ").strip().lower()

    year = None
    start_decade = None
    end_decade = None

    if user_input.isdigit():
        year = int(user_input)
    elif user_input.endswith("s") and user_input[:-1].isdigit():
        start_decade = int(user_input[:-1])
        end_decade = start_decade + 9

    user_pages = input("How many pages of results? (1 page = ~20 movies): ").strip()
    pages = int(user_pages) if user_pages.isdigit() else 1

    movies = search_movies(
        genre_id=genre_id,
        year=year,
        pages=pages,
        start_year=start_decade,
        end_year=end_decade
    )

    sorted_movies = sorted(movies, key=lambda m: m.get("vote_average", 0), reverse=True)
    display_movies(sorted_movies)

    choice = input("\nEnter the numbers of movies to save (comma-separated), or press Enter to skip: ").strip()

    if choice:
        indices = [i.strip() for i in choice.split(",") if i.strip().isdigit()]
        indices = [int(i) - 1 for i in indices if 0 <= int(i) - 1 < len(sorted_movies)]

        if not indices:
            print("❌ No valid movie numbers entered.")
        else:
            watchlist = load_watchlist()
            added = 0
            for idx in indices:
                movie = sorted_movies[idx]
                selected = {
                    "title": movie["title"],
                    "release_date": movie.get("release_date", "N/A"),
                    "vote_average": movie.get("vote_average", "N/A")
                }
                if selected not in watchlist:
                    watchlist.append(selected)
                    print(f"\n✅ Added: {selected['title']}")
                    print(f"📝 Summary: {movie.get('overview', 'No overview available.')}")
                    poster_path = movie.get("poster_path")
                    if poster_path:
                        print(f"🖼️ Poster: https://image.tmdb.org/t/p/w500{poster_path}")
                    else:
                        print("🖼️ No poster available.")
                    added += 1
            save_watchlist(watchlist)
            if added == 0:
                print("⚠️ All selected movies were already in your watchlist.")

def filter_movies_by_year(movies, year):
    return [movie for movie in movies if movie.get("release_date", "").startswith(str(year))]

def get_decade_range(decade_input):
    if decade_input.endswith("s") and decade_input[:-1].isdigit():
        start_year = int(decade_input[:-1])
        end_year = start_year + 9
        return start_year, end_year
    return None, None

if __name__ == "__main__":
    main()
