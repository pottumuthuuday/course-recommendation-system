import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("data/courses.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Combine features
df['tags'] = df['Title'] + " " + df['Skills'] + " " + df['Description']

# Convert text → vectors
tfidf = TfidfVectorizer(stop_words='english')
matrix = tfidf.fit_transform(df['tags'])

# Similarity
similarity = cosine_similarity(matrix)

# Recommendation function
def recommend(course_name):
    if course_name not in df['Title'].values:
        return ["Course not found"]

    index = df[df['Title'] == course_name].index[0]
    scores = list(enumerate(similarity[index]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []
    for i in sorted_scores[1:6]:
        recommendations.append(df.iloc[i[0]]['Title'])

    return recommendations