import numpy as np
import pandas as pd
from app.config import (
    SYNTHETIC_DATASET_SIZE,
    NORMAL_RATIO,
    DEVIATED_RATIO,
    TARGET_COMPOSITION,
    DATASET_PATH,
    RANDOM_STATE,
    ELEMENTS
)

np.random.seed(RANDOM_STATE)


def generate_normal_sample():
    sample = {}
    for element in ELEMENTS:
        min_val, max_val = TARGET_COMPOSITION[element]
        sample[element] = np.random.uniform(min_val, max_val)
    return sample


def generate_deviated_sample():
    sample = {}
    for element in ELEMENTS:
        min_val, max_val = TARGET_COMPOSITION[element]

        if np.random.rand() > 0.5:
            sample[element] = np.random.uniform(0, min_val)
        else:
            sample[element] = np.random.uniform(max_val, max_val + 3)

    return sample


def generate_dataset():
    normal_count = int(SYNTHETIC_DATASET_SIZE * NORMAL_RATIO)
    deviated_count = int(SYNTHETIC_DATASET_SIZE * DEVIATED_RATIO)

    data = []
    labels = []

    for _ in range(normal_count):
        data.append(generate_normal_sample())
        labels.append(0)

    for _ in range(deviated_count):
        data.append(generate_deviated_sample())
        labels.append(1)

    df = pd.DataFrame(data)
    df["anomaly"] = labels

    df.to_csv(DATASET_PATH, index=False)
    print("Dataset generated successfully.")


if __name__ == "__main__":
    generate_dataset()