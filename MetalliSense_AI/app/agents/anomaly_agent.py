from app.inference.anomaly_predict import detect_anomaly


def analyze_sample(sample):
    result = detect_anomaly(sample)

    if result == 1:
        return {"status": "Anomalous"}
    else:
        return {"status": "Normal"}