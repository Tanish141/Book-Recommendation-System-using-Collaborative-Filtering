# Import Libraries
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample Dataset of user ratings (replace with a real dataset if available)
df = pd.read_csv('Dataset/data.csv')

# Information of Dataset
print("\n", df.describe())
print("\n", df.info())
print("\n", df.head())

print(df.columns)

# Necessary Data
data = df[['isbn10', 'title', 'average_rating']]
print(data.head())

# Create a user-book matrix
user_book_matrix = data.pivot_table(index='isbn10', columns='title', values='average_rating', aggfunc='mean').fillna(0)
print("\n User-Book Matrix : \n", user_book_matrix)

# Calculate cosine similarity between users
user_similarity = cosine_similarity(user_book_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_book_matrix.index, columns=user_book_matrix.index)

print("\n User Similarity Matrix : \n", user_similarity_df)

# Function to recommend books based on user similarity
def recommend_books(user_id, similarity_matrix, user_book_matrix, top_n=3):
    user_id = str(user_id)  # Ensure compatibility with DataFrame index
    if user_id not in similarity_matrix.index:
        print("User not found in the dataset.")
        return []

    # Get similarity scores for user
    similar_users = similarity_matrix[user_id].sort_values(ascending=False).drop(user_id)

    # Aggregate ratings from similar users, weighted by similarity
    recommend_books = {}
    for sim_user, similarity in similar_users.items():
        if sim_user in user_book_matrix.index:
            rated_books = user_book_matrix.loc[sim_user]
            for book, rating in rated_books[rated_books > 0].items():
                if book not in user_book_matrix.loc[user_id] or user_book_matrix.loc[user_id, book] == 0:
                    recommend_books[book] = recommend_books.get(book, 0) + rating * similarity

    # Sort books by aggregated score and return top recommendations
    recommend_books = sorted(recommend_books.items(), key=lambda x: x[1], reverse=True)
    return [book for book, score in recommend_books[:top_n]]

# Get recommendations for a specific user
user_id = "0002261987"  # Ensure user_id is a string
recommend_books = recommend_books(user_id, user_similarity_df, user_book_matrix, top_n=3)
print(f"\n Books recommended for user {user_id} :", recommend_books)