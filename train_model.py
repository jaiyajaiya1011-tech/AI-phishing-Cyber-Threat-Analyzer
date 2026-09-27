import pandas as pd
import joblib
import re
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

print("Loading local phishing dataset...")

df = pd.read_csv(next(Path(".").rglob("*.csv")))

print("Dataset loaded!")
print("Rows:", len(df))

def extract_features(url):
    url = str(url).lower()

    return [
        len(url),
        url.count("."),
        url.count("/"),
        url.count("-"),
        url.count("@"),
        url.count("?"),
        url.count("="),
        url.count("&"),
        url.count("%"),
        url.count("_"),
        url.count("#"),
        int(url.startswith("https")),
        int(url.startswith("http://")),
        int(bool(re.search(r"\d+\.\d+\.\d+\.\d+", url))),
        int("login" in url),
        int("verify" in url),
        int("account" in url),
        int("secure" in url),
        int("update" in url),
        int("password" in url),
        int("bank" in url),
        int("free" in url),
        int("prize" in url),
        url.count("//")
    ]

print("Preparing URL features...")

X = df["URL"].apply(extract_features).tolist()

y = df["label"]

print("Features:", len(X[0]))
print("Training model...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

print("\n===== MODEL PERFORMANCE =====")
print(f"Accuracy : {accuracy * 100:.2f}%")
print(f"Precision: {precision * 100:.2f}%")
print(f"Recall   : {recall * 100:.2f}%")
print(f"F1 Score : {f1 * 100:.2f}%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

joblib.dump(model, "phishing_model.pkl")

print("\nModel saved successfully!")