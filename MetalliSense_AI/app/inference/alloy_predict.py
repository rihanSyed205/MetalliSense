import joblib
from app.config import MODEL_PATHS

model = joblib.load(MODEL_PATHS["alloy"])


def classify_sample(sample):
    prediction = model.predict([sample])[0]
    confidence = max(model.predict_proba([sample])[0])
    return prediction, confidence