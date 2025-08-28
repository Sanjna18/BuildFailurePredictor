# model_training.py

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

def train_model(df):
    X = df[["duration", "lines_added", "lines_removed", "files_changed"]]
    y = df["result"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print("Model Performance:\n", classification_report(y_test, preds))
    
    joblib.dump(model, "build_failure_predictor.pkl")
    return model
