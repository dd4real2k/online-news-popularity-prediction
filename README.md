# 📊 Online News Popularity Prediction

A complete end-to-end data science project using **Python, SQL, and Machine Learning** to analyse and predict the popularity of online news articles.

---

## 🚀 Project Overview
This project explores what drives engagement in online news by analysing over **39,000 articles** and building predictive models to estimate social media shares.

The goal is to simulate a real-world scenario where publishers can **predict article performance before publication** and optimise their content strategy.

---

## 🎯 Objectives
- Clean and prepare a real-world dataset
- Perform SQL-based exploratory analysis
- Visualise engagement trends
- Build machine learning models to predict article popularity
- Identify key factors influencing article shares

---

## 🛠️ Tech Stack
- **Python**: Pandas, NumPy, Scikit-learn
- **SQL**: SQLite
- **Visualisation**: Matplotlib, Seaborn
- **Machine Learning**: Linear Regression, Random Forest
- **Version Control**: Git & GitHub

---

## 📁 Project Structure

```text
online-news-popularity-prediction/
│
├── data/
│   ├── OnlineNewsPopularity.csv
│   └── cleaned_online_news.csv
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_sql_analysis.ipynb
│   ├── 03_eda_visualisation.ipynb
│   └── 04_model_building.ipynb
│
├── sql/
│   └── analysis_queries.sql
│
├── src/
│   └── random_forest_model.pkl
│
├── README.md
├── requirements.txt
└── .gitignore
```

## 🧹 Data Cleaning & Preparation
- Removed irrelevant columns (`url`, `timedelta`)
- Cleaned column names for SQL compatibility
- Verified no missing values or duplicates
- Applied log transformation to the target variable (`shares`) to handle skewness

---

## 🧠 SQL Analysis
SQL queries were used to extract insights such as:
- Top-performing article categories
- Best publishing days for engagement
- Impact of images and videos on shares
- Relationship between article length and popularity

Example:

```sql
SELECT
    COUNT(*) AS total_articles,
    ROUND(AVG(shares), 2) AS average_shares
FROM news;
```

## 📊 Exploratory Data Analysis

Key findings:

- Article shares are highly skewed
- Content category strongly influences engagement
- Multimedia (images/videos) shows moderate impact
- Publishing day affects performance

## 🤖 Machine Learning Models
**Models Used**
- Linear Regression (baseline)
- Random Forest Regressor

**Evaluation Metrics**
- RMSE (Root Mean Squared Error)
- R² Score

**Result**
Random Forest outperformed Linear Regression, capturing non-linear relationships in the data.

| Model | RMSE | R² Score |
|---|---:|---:|
| Linear Regression | add value | add value |
| Random Forest | add value | add value |

## 🔍 Feature Importance

Top factors influencing article popularity:
- Number of keywords
- Article length
- Social media references
- Multimedia usage

##  Business Impact
- This project demonstrates how data-driven insights can:
- Improve content strategy
- Increase audience engagement
- Support editorial decision-making
- Predict high-performing articles

## 📌 Future Improvements
- Hyperparameter tuning (GridSearchCV)
- Streamlit dashboard for live predictions
- API deployment (FastAPI)
- Integration with real-time data sources

## 📊 Visual Insights

### Distribution of Shares
![Shares Distribution](images/shares_distribution.png)

### Feature Importance
![Feature Importance](images/feature_importance.png)
