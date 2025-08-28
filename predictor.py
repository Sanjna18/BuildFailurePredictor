# predictor.py

import joblib
import numpy as np

def predict_failure(build_data):
    model = joblib.load("build_failure_predictor.pkl")
    features = np.array([[build_data["duration"],
                          build_data["lines_added"],
                          build_data["lines_removed"],
                          build_data["files_changed"]]])
    prediction = model.predict(features)[0]
    return prediction

def generate_recommendation(prediction, build_data):
    if prediction == 0:
        return "✅ Build likely to succeed."
    
    tips = []
    if build_data["lines_removed"] > 100:
        tips.append("Too many deletions. Double-check critical code removals.")
    if build_data["files_changed"] > 10:
        tips.append("Large number of file changes. Ensure all modules are tested.")
    if build_data["duration"] > 300000:
        tips.append("Long build time. Consider optimizing steps or splitting jobs.")
    
    return "⚠️ Build likely to fail. Suggestions: " + "; ".join(tips)
