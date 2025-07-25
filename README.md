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
   - Navigate to **Settings → API** and copy your API key
   - Create a file in the root directory named:  
     `.env`
   - Add this line inside the file (replace with your actual API key):

     ```
     TMDB_API_KEY=your_tmdb_api_key_here
     ```

---

## ▶️ Usage

Run the program with:

```bash
python project.py
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
├── project.py           
├── test_project.py      # Tests for at least 3 custom functions
├── .env                 # Holds API key
├── .gitignore           
├── requirements.txt     # Lists all required dependencies
├── README.md            
└── watchlist.json       # storage
```

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍🎓 Credits

Created by [@pariasalsabili](https://github.com/pariasalsabili)  
Final Project for [CS50P: Introduction to Programming with Python](https://cs50.harvard.edu/python/)

Thanks to [TMDb](https://www.themoviedb.org/) for the API and movie data.
