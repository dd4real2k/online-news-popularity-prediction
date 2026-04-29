import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os

# -----------------------------
# Load Model
# -----------------------------
MODEL_PATH = "src/random_forest_model.pkl"
DATA_PATH = "data/processed/cleaned_online_news.csv"

model = joblib.load(MODEL_PATH)
df = pd.read_csv(DATA_PATH)

# -----------------------------
# App Title
# -----------------------------
st.set_page_config(page_title="News Popularity Predictor", layout="wide")

st.title("📊 Online News Popularity Dashboard")
st.write("Predict how popular an article will be based on its features.")

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("🔧 Input Article Features")

n_tokens_title = st.sidebar.slider("Title Length", 5, 30, 10)
n_tokens_content = st.sidebar.slider("Content Length", 100, 3000, 800)
num_hrefs = st.sidebar.slider("Number of Links", 0, 50, 10)
num_imgs = st.sidebar.slider("Number of Images", 0, 10, 2)
num_videos = st.sidebar.slider("Number of Videos", 0, 5, 1)
num_keywords = st.sidebar.slider("Number of Keywords", 1, 10, 5)

category = st.sidebar.selectbox(
    "Article Category",
    ["Lifestyle", "Entertainment", "Business", "Social Media", "Tech", "World"]
)

weekday = st.sidebar.selectbox(
    "Publishing Day",
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)

# -----------------------------
# Prepare Input
# -----------------------------
input_dict = {
    "n_tokens_title": n_tokens_title,
    "n_tokens_content": n_tokens_content,
    "num_hrefs": num_hrefs,
    "num_imgs": num_imgs,
    "num_videos": num_videos,
    "num_keywords": num_keywords
}

# Category encoding
categories = [
    "data_channel_is_lifestyle",
    "data_channel_is_entertainment",
    "data_channel_is_bus",
    "data_channel_is_socmed",
    "data_channel_is_tech",
    "data_channel_is_world"
]

for cat in categories:
    input_dict[cat] = 0

category_map = {
    "Lifestyle": "data_channel_is_lifestyle",
    "Entertainment": "data_channel_is_entertainment",
    "Business": "data_channel_is_bus",
    "Social Media": "data_channel_is_socmed",
    "Tech": "data_channel_is_tech",
    "World": "data_channel_is_world"
}

input_dict[category_map[category]] = 1

# Weekday encoding
weekdays = [
    "weekday_is_monday",
    "weekday_is_tuesday",
    "weekday_is_wednesday",
    "weekday_is_thursday",
    "weekday_is_friday",
    "weekday_is_saturday",
    "weekday_is_sunday"
]

for day in weekdays:
    input_dict[day] = 0

weekday_map = {
    "Monday": "weekday_is_monday",
    "Tuesday": "weekday_is_tuesday",
    "Wednesday": "weekday_is_wednesday",
    "Thursday": "weekday_is_thursday",
    "Friday": "weekday_is_friday",
    "Saturday": "weekday_is_saturday",
    "Sunday": "weekday_is_sunday"
}

input_dict[weekday_map[weekday]] = 1

input_df = pd.DataFrame([input_dict])

# Align with model features
for col in model.feature_names_in_:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[model.feature_names_in_]

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔮 Predict Popularity"):
    prediction_log = model.predict(input_df)[0]
    prediction = np.expm1(prediction_log)

    st.success(f"Estimated Shares: {int(prediction):,}")

# -----------------------------
# Visual Insights
# -----------------------------
st.header("📊 Visual Insights")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/shares_distribution.png", caption="Shares Distribution")

with col2:
    st.image("images/feature_importance.png", caption="Feature Importance")

with col3:
    st.image("images/model_comparison.png", caption="Model Comparison")

# -----------------------------
# Dataset Preview
# -----------------------------
st.header("📂 Dataset Preview")
st.dataframe(df.head())
