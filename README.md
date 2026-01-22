#FF7-Rebirth-Emotional-Analysis

**Project Portfolio – Emotional Analysis of FF7 Rebirth Game Reviews**

---

## 🚀 Introduction

Inspired by this video: <link>.

I created a small **Emotional Analysis** project specifically for reviews of the game *Final Fantasy VII Rebirth*.

The goal was to collect and analyze player feedback to determine the level of **positive/negative/neutral** sentiment regarding this game.

---

## 📂 Folder Structure

├── data/
│ └── (input data – reviews)
├── helpers/
│ └── (preprocessing and processing support scripts)
├── 1_Languages.ipynb
├── 2_n_grams.ipynb
├── 3_price.ipynb
├── 4_playtime.ipynb
├── 5_wordcloud.ipynb
├── 6_funniest.ipynb
├── 7_ff7Remake.ipynb
├── 8_ascii_art.ipynb
├── 9_complaint.ipynb
├── 10_characters.ipynb
├── 11_bosses.ipynb
├── fetch_reviews.py
├── ff7rebirth_output.csv
├── ff7remake_output.csv
├── reviews.duckdb
└── README.md

> 📌 The `.ipynb` notebooks contain various analysis sections such as:

> • Languages
> • n-grams
> • Wordcloud visualization
> • Comparison of sentiment between *FF7 Rebirth* and *FF7 Remake*
> • Analysis of “funniest”, “complaints”, “characters”, “bosses”…

---

## 🧠 Project Objectives

1. **Collect player reviews** for *FF7 Rebirth* and *FF7 Remake*.
2. **Preprocess text data**: tokenization, stopword filtering, normalization.
3. **Sentiment Analysis**:
- Calculate polarity score for reviews
- Classify sentiment as positive/negative/neutral
  
4. **Visualize Results**
- Wordcloud chart
- Comparisons between different review types
- Sentiment scores by “characters”, “bosses”, etc.
  
5. **Compare Sentiment between FF7 Rebirth & FF7 Remake**

---

## 📊 How to run 
1. Collect reviews
python fetch_reviews.py

The fetch_reviews.py script will load reviews from the data source and save them in reviews.duckdb or .csv.

## 📈 Analysis

Open and run each Notebook to see the details:

jupyter notebook

Examples:
5_wordcloud.ipynb → create Wordcloud
6_funniest.ipynb → analyze “funny” reviews
7_ff7Remake.ipynb → compare with FF7 Remake

## 🧪 Technologies used

* Python
* Jupyter Notebook
* NLP/Text processing (Tokenize, n-grams, Wordcloud…)
* DuckDB / CSV file handling
