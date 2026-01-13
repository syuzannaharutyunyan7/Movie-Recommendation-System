# 🎬 Movie Recommendation System

## Overview

This project is a **content-based movie recommendation system** built using Python and Streamlit. It uses the **MovieLens 100k dataset** to recommend movies to users based on genre similarity.

The goal of this project is to demonstrate practical skills in:

* Data processing with **Pandas**
* Feature extraction using **TF-IDF**
* Computing similarity with **cosine similarity**
* Building interactive web apps using **Streamlit**

---

## Features

* Select a movie you like from a dropdown list.
* Get **10 recommended movies** that are similar in genres.
* Simple, fast, and user-friendly interface.

---

## Dataset

* **MovieLens 100k dataset**: 100,000 ratings from 1000 users on 1700 movies.
* `u.item`: Contains movie information such as movie ID, title, and genres.
* `u.data`: Optional ratings data (not used in this version).

> Dataset source: [MovieLens 100k](https://grouplens.org/datasets/movielens/100k/)

---

## Installation

1. **Clone or download the project folder**.
2. **Navigate to the project folder**:

```bash
cd ~/Desktop/movie_recommender
```

3. **Create and activate a virtual environment**:

```bash
python3 -m venv venv
source venv/bin/activate
```

4. **Install required packages**:

```bash
pip install pandas numpy scikit-learn streamlit
```

---

## Running the App

Start the Streamlit app with:

```bash
streamlit run app.py
```

* A new browser window will open at `http://localhost:8501`.
* Select a movie and click **Show Recommendations** to see the top 10 similar movies.

---

## Project Structure

```
movie_recommender/
├─ app.py          # Main Streamlit app
├─ u.item          # MovieLens 100k movie information
├─ u.data          # Optional ratings data
├─ venv/           # Python virtual environment
├─ README.md       # Project documentation
```

---

## Future Improvements

* Add **collaborative filtering** using the `u.data` ratings file.
* Combine content-based and collaborative filtering for a **hybrid recommendation system**.
* Include movie posters and metadata for a more visual interface.

---

## Author

**Syuzanna Harutyunyan** 
 
