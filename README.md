# Wildfire Risk Prediction

End-to-end machine learning pipeline to predict daily wildfire risk using real climate, vegetation, and fire detection data.

## Data Sources
- NASA FIRMS (fire detections)
- ERA5 (weather)
- MODIS NDVI (vegetation)
- US Drought Monitor

## Problem
Binary classification: predict probability of wildfire occurrence for a given location and day.

## Features
- Temperature
- Wind speed
- Precipitation
- NDVI
- Drought index

## Model
Feedforward neural network implemented in PyTorch.

## Evaluation
ROC-AUC, Precision-Recall AUC, calibration analysis.

## Pipeline
1. Download raw datasets
2. Spatial + temporal joins
3. Feature engineering
4. Model training
5. Evaluation

## Run
python main.py