🎬 Movie Recommendation System
This project is a Content-Based Movie Recommendation System built using Python. It suggests movies similar to a user's favorite by analyzing movie metadata such as genres, cast, and crew.

📌 Features
Content-based filtering using movie metadata
Similarity computation using cosine similarity
Interactive user interface with Streamlit
Integration with TMDB API for fetching movie details

🛠️ Installation
Clone the repository:
git clone https://github.com/mdishaq33/Movie-Recommendation-System.git
cd Movie-Recommendation-System

Install the required packages:
pip install -r requirements.txt

Set up TMDB API key:
Create a file named .streamlit/secrets.toml in the project root.
Add your TMDB API key to this filetmdb_api_key = "your_api_key_here"

🚀 Usage
Run the Streamlit application:
streamlit run app.py
The application will open in your default web browser at http://localhost:8501.

📂 Dataset
The project uses the TMDB 5000 Movie Dataset, which includes information about movies such as genres, cast, crew, and overviews.
