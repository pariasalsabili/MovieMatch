# 🎬 MovieMatch

**MovieMatch** is a Python command-line app that helps users discover top-rated movies by genre, year, or decade using the TMDb API. Designed as a final project for Harvard's **CS50P (Introduction to Programming with Python)**, it also includes a persistent personal watchlist.

---

## 📌 Features

- 🎭 Search movies by genre  
- 🗓️ Filter results by year or decade  
- 📊 Sort movies by TMDb rating (highest first)  
- ✅ Add one or more movies to a watchlist  
- 📝 View summary and poster link for selected movies  
- 📂 Edit or remove items from the watchlist (CRUD support)  
- 💾 Persistent local storage using `watchlist.json`

---

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/pariasalsabili/MovieMatch.git
cd MovieMatch
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Get your TMDb API Key**
   - Sign up at [themoviedb.org](https://www.themoviedb.org)
   - Navigate to **Settings → API**
   - Paste your API key into `TMDB_API.py`:
```python
API_KEY = "your_api_key_here"
```

---

## ▶️ Usage

Run the program with:
```bash
python main.py
```

You'll be prompted to:
- Choose a genre  
- Enter a year or decade  
- Select movies to add to your watchlist  

Your watchlist will be saved to a local file (`watchlist.json`), and can be viewed or edited within the app.

---

## 📁 Project Structure

```
MovieMatch/
├── main.py             # Main app logic
├── TMDB_API.py         # Handles API calls
├── watchlist.json      # Saved watchlist (local storage)
├── requirements.txt    # Dependencies
└── README.md           # You're here!
```

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍🎓 Credits

Created by [@pariasalsabili](https://github.com/pariasalsabili)  
Final Project for [CS50P: Introduction to Programming with Python](https://cs50.harvard.edu/python/)

Thanks to [TMDb](https://www.themoviedb.org/) for the API and movie data.
