# 📊 Online News Popularity Prediction

## 🚀 Project Overview
This project analyses and predicts the popularity of online news articles using **Python, SQL, and Machine Learning**. The goal is to uncover key factors that drive engagement and build predictive models for article shares.

The dataset contains over **39,000 articles** with features related to content, publishing patterns, and metadata.

---

## 🎯 Objectives
- Perform data cleaning and preprocessing
- Conduct SQL-based exploratory analysis
- Visualise patterns in article engagement
- Build machine learning models to predict popularity
- Identify key drivers of article shares

---

## 🛠️ Tech Stack
- Python (Pandas, NumPy, Scikit-learn)
- SQL (SQLite)
- Matplotlib & Seaborn
- Machine Learning (Linear Regression, Random Forest)
- Git & GitHub

---

## 📁 Project Structure


---

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
