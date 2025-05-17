# 🎬 Movie Recommender System

This project is a **Content-Based Movie Recommender System** built using the **TMDB 5000 Movie Dataset**. It recommends 10 similar movies based on the movie selected by the user. The project also includes a **Streamlit** web app for interactive use and utilizes **TMDB API** to fetch movie posters and information.

---

## 📊 Dataset

The project uses:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

These datasets are merged and processed using the following columns to create a content tag:
- `overview`
- `genres`
- `keywords`
- `cast`
- `crew`

## 🧠 NLP Techniques Used

- **Tokenization**
- **Stopword Removal**
- **Stemming** (using PorterStemmer)
- **CountVectorizer** to convert tags into numerical vectors
- **Cosine Similarity** to calculate distance between movies based on content

## 🚀 Features

- Recommends top 10 similar movies based on selected movie
- Uses **cosine similarity** to find closeness in content
- Interactive **Streamlit** interface
- Movie posters fetched using **TMDB API**
