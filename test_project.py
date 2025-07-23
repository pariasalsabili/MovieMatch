import pytest
import json
from project import load_watchlist, save_watchlist, filter_movies_by_year, get_decade_range

def test_save_and_load_watchlist(tmp_path):
    test_file = tmp_path / "watchlist.json"
    test_data = [{"id": 1, "title": "Test Movie", "year": 2022, "rating": 8.5}]
    save_watchlist(test_data, filepath=test_file)
    loaded = load_watchlist(filepath=test_file)
    assert loaded == test_data

def test_filter_movies_by_year():
    movies = [
        {"title": "A", "year": 2010},
        {"title": "B", "year": 2015},
        {"title": "C", "year": 2020}
    ]
    result = filter_movies_by_year(movies, 2015)
    assert len(result) == 1
    assert result[0]["title"] == "B"

def test_get_decade_range():
    assert get_decade_range("1990s") == (1990, 1999)
    assert get_decade_range("2000s") == (2000, 2009)
    assert get_decade_range("1980s") == (1980, 1989)