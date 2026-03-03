import joblib
from app.config import MODEL_PATHS

model = joblib.load(MODEL_PATHS["anomaly"])


def detect_anomaly(sample):
    prediction = model.predict([sample])
    return 1 if prediction[0] == -1 else 0