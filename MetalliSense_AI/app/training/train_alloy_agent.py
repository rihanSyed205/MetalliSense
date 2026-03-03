import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from app.config import (
    MODEL_PATHS,
    RANDOM_STATE,
    DATASET_PATH,
    ELEMENTS
)

df = pd.read_csv(DATASET_PATH)

X = df[ELEMENTS]
y = df["anomaly"]

model = RandomForestClassifier(
    n_estimators=200,
    random_state=RANDOM_STATE
)

model.fit(X, y)

joblib.dump(model, MODEL_PATHS["alloy"])
print("Alloy agent model trained and saved.")