# 🎬 Movie Recommender System (Gradio Web App)

This is a simple content-based Movie Recommender System built with TF-IDF vectorization and cosine similarity. The app is powered by **Gradio** and deployed on **Hugging Face Spaces**.

---

## 🚀 Live Demo
🔗 [Try the App on Hugging Face Spaces](https://huggingface.co/spaces/your-username/movie-recommender) *(replace with your actual link)*

---

## 📦 Features
- Content-based movie recommendations
- TF-IDF vectorization on movie plot overviews
- Cosine similarity to find similar movies
- User-friendly Gradio web interface
- Deployed on Hugging Face (public)

---

## 🧠 Concepts Learned
- TF-IDF Vectorization
- Cosine Similarity for text
- Mapping string inputs to recommendations
- Web deployment using Gradio
- Hugging Face Space structure

---

## 📊 Dataset
A sample movie dataset containing 5 movies:
- Avatar
- The Dark Knight
- Avengers: Endgame
- Titanic
- Interstellar

Each entry contains:
- Title
- Plot overview

*For a full-scale project, you can use TMDB 5000 Movie Dataset or Kaggle IMDB movies.*

---

## 🧩 App Logic Flow
```text
1. Load movie dataset (title + overview)
2. Vectorize overviews using TF-IDF
3. Compute cosine similarity matrix
4. Build recommend(title) function
5. Build Gradio UI
6. Deploy on Hugging Face
```

---

## 💻 Run Locally
```bash
pip install -r requirements.txt
python app.py
```

---

## 📁 Files
```
├── app.py                  # Gradio web app
├── tmdb_sample_movies.csv  # Sample dataset (5 movies)
├── requirements.txt        # Gradio + scikit-learn + pandas
```

---

## 📸 Screenshot
![Movie Recommender](screenshot.png)

---

## 👤 Author
Built by Mamata *(ChatGPT-powered AI learner)*

---

## 📝 License
This project is for educational use and MIT-licensed.
