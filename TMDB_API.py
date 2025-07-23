import requests

API_KEY = "bf87a0134ddd7931f8dd9fb5b8d6d8be"
BASE_URL = "https://api.themoviedb.org/3"

def get_genres():
    url = f"{BASE_URL}/genre/movie/list"
    params = {"api_key": API_KEY}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    genres = data["genres"]
    genre_map = {genre["name"].lower(): genre["id"] for genre in genres}
    return genre_map

def search_movies(genre_id=None, year=None, pages=1, start_year=None, end_year=None):
    all_results = []
    for page in range(1, pages + 1):
        url = f"{BASE_URL}/discover/movie"
        params = {
            "api_key": API_KEY,
            "sort_by": "popularity.desc",
            "page": page
        }
        if genre_id:
            params["with_genres"] = genre_id
        if year:
            params["primary_release_year"] = year
        if start_year and end_year:
            params["primary_release_date.gte"] = f"{start_year}-01-01"
            params["primary_release_date.lte"] = f"{end_year}-12-31"

        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        all_results.extend(data.get("results", []))

        if page >= data.get("total_pages", 1) or page >= 500:
            break

    return all_results

