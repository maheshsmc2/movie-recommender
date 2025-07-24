
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import gradio as gr

# Load dataset
movies = pd.read_csv("tmdb_sample_movies.csv")
movies = movies.reset_index()
movies['overview'] = movies['overview'].fillna('')

# Vectorize
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['overview'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(movies.index, index=movies['title'])

# Recommendation function
def recommend_ui(movie_title):
    if movie_title not in indices:
        return ["Movie not found. Try another title."]
    idx = indices[movie_title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    recommended = [movies['title'][i] for i, score in sim_scores]
    return recommended

# Movie list for dropdown
movie_list = movies['title'].tolist()

# Gradio interface
iface = gr.Interface(
    fn=recommend_ui,
    inputs=gr.Dropdown(choices=movie_list, label="Pick a movie"),
    outputs=gr.Textbox(label="Recommended Movies"),
    title="🎬 Movie Recommender",
    description="Select a movie to get similar recommendations!"
)

if __name__ == "__main__":
    iface.launch()
