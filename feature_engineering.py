# feature_engineering.py

import pandas as pd
from datetime import datetime

def extract_features_from_build(build):
    return {
        "build_number": build.get("number"),
        "duration": build.get("duration", 0),
        "timestamp": datetime.fromtimestamp(build["timestamp"] / 1000),
        "result": 0 if build.get("result") == "SUCCESS" else 1,
        "lines_added": build.get("lines_added", 0),
        "lines_removed": build.get("lines_removed", 0),
        "files_changed": build.get("files_changed", 0)
    }

def prepare_dataset(builds):
    features = [extract_features_from_build(b) for b in builds]
    df = pd.DataFrame(features)
    df = df.dropna()
    return df
