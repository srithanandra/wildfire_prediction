IN ORDER TO RUN:
- Run "pip install -r requirements.txt" in the terminal
- Then, run "main.py"

WILDFIRE RISK PREDICTION:
- End-to-end machine learning pipeline to predict daily wildfire risk using real climate, vegetation, and fire detection data.

DATA SOURCES:
- NASA FIRMS (fire detections)
- ERA5 (weather)
- MODIS NDVI (vegetation)
- US Drought Monitor

FEATURES:
- Temperature
- Wind speed
- Precipitation
- NDVI
- Drought index

MODEL:
- Feedforward neural network implemented in PyTorch.

EVALUATION:
- ROC-AUC, Precision-Recall AUC, calibration analysis.

PIPELINE:
1. Download raw datasets
2. Spatial + temporal joins
3. Feature engineering
4. Model training
5. Evaluation