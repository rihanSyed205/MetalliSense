import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest
from app.config import (
    MODEL_PATHS,
    ANOMALY_CONTAMINATION,
    RANDOM_STATE,
    DATASET_PATH,
    ELEMENTS
)

df = pd.read_csv(DATASET_PATH)
X = df[ELEMENTS]

model = IsolationForest(
    contamination=ANOMALY_CONTAMINATION,
    random_state=RANDOM_STATE
)

model.fit(X)

joblib.dump(model, MODEL_PATHS["anomaly"])
print("Anomaly model trained and saved.")