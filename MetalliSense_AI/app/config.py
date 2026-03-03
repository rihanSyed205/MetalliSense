"""
Configuration settings for MetalliSense AI Service
"""

import os
from pathlib import Path

# -----------------------------
# Base Directories
# -----------------------------

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"

DATA_DIR.mkdir(parents=True, exist_ok=True)
MODELS_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Model Paths
# -----------------------------

MODEL_PATHS = {
    "anomaly": MODELS_DIR / "anomaly_model.pkl",
    "alloy": MODELS_DIR / "alloy_model.pkl"
}

DATASET_PATH = DATA_DIR / "dataset.csv"

# -----------------------------
# Elements Tracked
# -----------------------------

ELEMENTS = ["Fe", "C", "Si", "Mn", "P", "S"]

# -----------------------------
# Synthetic Data Generation
# -----------------------------

SYNTHETIC_DATASET_SIZE = 200000
NORMAL_RATIO = 0.65
DEVIATED_RATIO = 0.35

ANOMALY_CONTAMINATION = DEVIATED_RATIO
RANDOM_STATE = 42

# -----------------------------
# Anomaly Severity Thresholds
# -----------------------------

ANOMALY_SEVERITY_THRESHOLDS = {
    "LOW": 0.0,
    "MEDIUM": 0.33,
    "HIGH": 0.66
}

# -----------------------------
# Confidence Levels
# -----------------------------

CONFIDENCE_THRESHOLDS = {
    "HIGH": 0.85,
    "MEDIUM": 0.70,
    "LOW": 0.50
}

MIN_CONFIDENCE_THRESHOLD = 0.5

# -----------------------------
# Safety Constraints
# -----------------------------

MAX_ADDITION_PERCENTAGE = 5.0
MAX_REDUCTION_PERCENTAGE = 5.0
TOTAL_COMPOSITION_TOLERANCE = 0.5

# -----------------------------
# Target Composition Template
# -----------------------------

TARGET_COMPOSITION = {
    "Fe": (95.0, 99.0),
    "C": (0.2, 0.8),
    "Si": (0.1, 1.0),
    "Mn": (0.2, 1.5),
    "P": (0.0, 0.05),
    "S": (0.0, 0.05)
}

# -----------------------------
# API Settings
# -----------------------------

API_HOST = "0.0.0.0"
API_PORT = 8000
API_TITLE = "MetalliSense AI Service"
API_VERSION = "1.0.0"