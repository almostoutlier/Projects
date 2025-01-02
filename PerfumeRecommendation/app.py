from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.config['DEBUG'] = True

# Data loading and cleaning
def clean_data(df):
    df.rename(
        columns={
            "mainaccord5,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,": "mainaccord5"
        },
        inplace=True,
    )
    df["mainaccord5"] = df["mainaccord5"].str.replace(",", "")
    df["Rating Value"] = df["Rating Value"].str.replace(",", ".")
    df["Rating Value"] = df["Rating Value"].astype(float)
    df = df.dropna(subset=["Year"])
    df['Year'] = df['Year'].astype(int)

    df['description'] = (
        df[['Top', 'Middle', 'Base', 'mainaccord1', 'mainaccord2', 'mainaccord3', 'mainaccord4', 'mainaccord5']]
        .fillna('')  
        .agg(' '.join, axis=1)  
    )
    df['description'] = df['description'].str.lower()  
    return df

def filter_perfumes(df, gender, brand, user_input):
    df = clean_data(df)
    filtered_df = df[df['Gender'].str.lower() == gender]
    
    if brand:
        filtered_df = filtered_df[filtered_df['Brand'].str.lower() == brand]

    if filtered_df.empty:
        return None

    # Vectorize text using TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(filtered_df['description'])

    # Vectorize user input
    user_vector = vectorizer.transform([user_input])

    # Compute cosine similarity
    similarity_scores = cosine_similarity(user_vector, tfidf_matrix)

    # Find the closest matching perfumes
    top_matches = np.argsort(similarity_scores[0])[::-1][:5]  # Top 5 matches
    results = []

    for idx in top_matches:
        match = filtered_df.iloc[idx]
        results.append({
            "perfume_name": match['Perfume'],
            "url": match['url'],
            "brand": match['Brand'],
            "rating_value": match['Rating Value'],
            "rating_count": match['Rating Count'],
            "description": match['description'],
            "similarity": similarity_scores[0][idx]
        })

    return results

# Flask routes
@app.route("/", methods=["GET", "POST"])
def recommend_perfume():
    if request.method == "POST":
        gender = request.form.get("gender", "").strip().lower()
        brand = request.form.get("brand", "").strip().lower()
        user_input = request.form.get("description", "").strip().lower()

        # Load the dataset
        df = pd.read_csv("fra_cleaned.csv", sep=';', encoding='latin-1')

        # Get recommendations
        recommendations = filter_perfumes(df, gender, brand, user_input)

        if recommendations:
            return render_template("results.html", recommendations=recommendations)
        else:
            return render_template("index.html", error="No matching perfumes found. Try different inputs.")
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
