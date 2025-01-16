# 📚 Book Recommendation System

This project implements a **Book Recommendation System** using **Collaborative Filtering**. The system leverages user-book rating data to recommend books based on cosine similarity between users. 🚀

---

## ✨ Features

- **User-Book Matrix** 📊: A pivot table is created to represent user ratings for books.
- **Cosine Similarity** 🔍: Measures similarity between users based on their book ratings.
- **Book Recommendations** 📚: Recommends books for a user by aggregating ratings from similar users.
- **Dynamic Recommendations** ⚙️: Supports customization for the number of recommendations.

---

## 🛠️ Technologies Used

- **Python** 🐍: Core programming language.
- **Pandas**: Data manipulation and pivot table creation.
- **Scikit-learn**: Cosine similarity calculation.

---

## 🚀 How It Works

1. **Input Dataset**: A CSV file containing user ratings for books with columns `isbn10`, `title`, and `average_rating`.
2. **User-Book Matrix**: A pivot table where rows represent users (`isbn10`), columns represent books (`title`), and values represent ratings (`average_rating`).
3. **Cosine Similarity**: Calculates pairwise similarity scores between users.
4. **Recommendations**: For a given user, recommends books that highly similar users have rated.

---

## 📂 File Structure

```
BookRecommendationSystem/
├── BookRecommendationSystem.py   # Main script for recommendations
├── Dataset/
│   └── data.csv                  # Dataset with user ratings
├── README.md                     # Project documentation
```

---

## ⚙️ Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Tanish141/BookRecommendationSystem.git
   cd BookRecommendationSystem
   ```

2. **Create a Virtual Environment (Optional)**:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\\Scripts\\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install pandas scikit-learn
   ```

4. **Run the Script**:
   ```bash
   python BookRecommendationSystem.py
   ```

---

## 🔠 Example Usage

### Input:
- **Dataset**:
  ```csv
  isbn10,title,average_rating
  0002005883,"Book A",4.5
  0002261987,"Book B",3.8
  ...
  ```
- **User ID**: `0002261987`

### Output:
```plaintext
User-Book Matrix:
title       Book A   Book B
isbn10                      
0002005883      4.5     0.0
0002261987      0.0     3.8
...

Books recommended for user 0002261987: ['Book A', 'Book C', 'Book D']
```

---

## 🌟 Key Learning Outcomes

- Building user-book matrices and handling sparse data.
- Computing cosine similarity for collaborative filtering.
- Recommending items based on aggregated user preferences.

---

## 🤝 Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project. ✨

---

## 📧 Contact

- **Email**: mrtanish14@gmail.com
- **GitHub**: https://github.com/Tanish141

---

🎉 **Happy Reading and Recommending!**

