import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.feature_selection import SelectKBest, f_classif
import joblib
import logging


# Set up logging
logging.basicConfig(level=logging.INFO)

# Load data
data = pd.read_csv(input("path to data:"))
labels = pd.read_csv(input("path to labels:"))

# Validate data
assert len(data) == len(labels), "Mismatched samples!"
assert "sample_id" in data.columns, "sample_id column missing!"
assert "disease_status" in labels.columns, "disease_status column missing!"

# Separate features and target
X = data.drop(columns=["sample_id"])
y = labels["disease_status"]

# Encode categorical labels
if y.dtype == "object":
    le = LabelEncoder()
    y = le.fit_transform(y)
    joblib.dump(le, "models/label_encoder.pkl")

# Check class balance
logging.info(f"Class distribution:\n{pd.Series(y).value_counts()}")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
joblib.dump(scaler, "models/scaler.pkl")

# Feature selection (optional)
selector = SelectKBest(f_classif, k=100)
X_train = selector.fit_transform(X_train, y_train)
X_test = selector.transform(X_test)
joblib.dump(selector, "models/feature_selector.pkl")

logging.info(
    f"Final shapes - X_train: {X_train.shape}, X_test: {X_test.shape}")
logging.info(
    f"Final shapes - y_train: {y_train.shape}, y_test: {y_test.shape}")


# Save preprocessed data
pd.DataFrame(X_train).to_csv("data/X_train.csv", index=False)
pd.DataFrame(X_test).to_csv("data/X_test.csv", index=False)
pd.DataFrame(y_train).to_csv("data/y_train.csv", index=False)
pd.DataFrame(y_test).to_csv("data/y_test.csv", index=False)
logging.info("Preprocessing completed successfully!")

