import joblib
import pandas as pd
import numpy as np
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "src" / "random_forest_model.pkl"


def load_model():
    """Load trained Random Forest model."""
    return joblib.load(MODEL_PATH)


def prepare_input(input_data, model):
    """
    Prepare input data so it matches the exact features used during training.
    Missing features are filled with 0.
    """
    input_df = pd.DataFrame([input_data])

    # Get feature names from the trained sklearn model
    expected_features = model.feature_names_in_

    # Add missing columns
    for feature in expected_features:
        if feature not in input_df.columns:
            input_df[feature] = 0

    # Keep only expected columns and correct order
    input_df = input_df[expected_features]

    return input_df


def predict_popularity(input_data):
    """
    Predict article popularity.
    Returns predicted log shares and estimated actual shares.
    """
    model = load_model()
    input_df = prepare_input(input_data, model)

    predicted_log_shares = model.predict(input_df)[0]
    predicted_shares = np.expm1(predicted_log_shares)

    return predicted_log_shares, predicted_shares


if __name__ == "__main__":
    sample_article = {
        "n_tokens_title": 10,
        "n_tokens_content": 800,
        "num_hrefs": 12,
        "num_self_hrefs": 3,
        "num_imgs": 4,
        "num_videos": 1,
        "average_token_length": 4.5,
        "num_keywords": 7,
        "data_channel_is_entertainment": 1,
        "weekday_is_tuesday": 1,
        "is_weekend": 0
    }

    log_prediction, share_prediction = predict_popularity(sample_article)

    print(f"Predicted log shares: {log_prediction:.2f}")
    print(f"Estimated actual shares: {share_prediction:.0f}")
