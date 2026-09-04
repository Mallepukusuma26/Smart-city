"""
ML Data Preprocessing and Feature Engineering Utilities.
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

class SmartCityPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoders = {}
        self.imputer = SimpleImputer(strategy="mean")

    def extract_datetime_features(self, df, datetime_col="recorded_at"):
        if datetime_col in df.columns:
            df[datetime_col] = pd.to_datetime(df[datetime_col], errors="coerce")
            df["hour"] = df[datetime_col].dt.hour
            df["day_of_week"] = df[datetime_col].dt.dayofweek
            df["month"] = df[datetime_col].dt.month
            df["is_weekend"] = df["day_of_week"].apply(lambda x: 1 if x >= 5 else 0)
        return df

    def encode_categorical_features(self, df, cat_cols):
        for col in cat_cols:
            if col in df.columns:
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col].astype(str))
                self.label_encoders[col] = le
        return df

    def fit_transform_numeric(self, X):
        X_imputed = self.imputer.fit_transform(X)
        return self.scaler.fit_transform(X_imputed)

    def transform_numeric(self, X):
        X_imputed = self.imputer.transform(X)
        return self.scaler.transform(X_imputed)
