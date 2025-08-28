# main.py

from feature_engineering import prepare_dataset
from model_training import train_model
from predictor import predict_failure, generate_recommendation

# 🔧 Dummy build data to simulate real Jenkins data
builds = [
    {
        "number": 1,
        "result": "SUCCESS",
        "duration": 120000,
        "timestamp": 1720425600000,
        "lines_added": 30,
        "lines_removed": 5,
        "files_changed": 3
    },
    {
        "number": 2,
        "result": "FAILURE",
        "duration": 300000,
        "timestamp": 1720512000000,
        "lines_added": 100,
        "lines_removed": 150,
        "files_changed": 12
    },
    {
        "number": 3,
        "result": "SUCCESS",
        "duration": 200000,
        "timestamp": 1720598400000,
        "lines_added": 10,
        "lines_removed": 3,
        "files_changed": 1
    }
]

if __name__ == "__main__":
    # Prepare dataset from dummy builds
    df = prepare_dataset(builds)

    # Train and save model
    model = train_model(df)

    # Pick the latest build and predict
    latest = df.iloc[-1].to_dict()
    prediction = predict_failure(latest)
    print("Prediction:", "Fail ❌" if prediction else "Success ✅")
    print(generate_recommendation(prediction, latest))
