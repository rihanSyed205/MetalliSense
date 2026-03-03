from app.inference.alloy_predict import classify_sample
from app.config import (
    TARGET_COMPOSITION,
    MAX_ADDITION_PERCENTAGE,
    MAX_REDUCTION_PERCENTAGE,
    ELEMENTS
)


def analyze_alloy(sample_list):
    prediction, confidence = classify_sample(sample_list)

    sample_dict = dict(zip(ELEMENTS, sample_list))

    recommendations = {}

    for element, value in sample_dict.items():
        target_min, target_max = TARGET_COMPOSITION[element]

        if value < target_min:
            diff = min(target_min - value, MAX_ADDITION_PERCENTAGE)
            recommendations[element] = f"Add {round(diff,2)}%"

        elif value > target_max:
            diff = min(value - target_max, MAX_REDUCTION_PERCENTAGE)
            recommendations[element] = f"Reduce {round(diff,2)}%"

    return {
        "prediction": int(prediction),
        "confidence": float(confidence),
        "recommendations": recommendations
    }