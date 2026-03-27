
# Wildfire Prediction

End-to-end machine learning pipeline to predict daily wildfire risk from fire detections and weather data.

## Project Structure

- `src/download/` - data download scripts
- `src/preprocess/` - feature-building and labeling
- `src/model/` - training and evaluation code
- `src/main/main.py` - full pipeline entrypoint
- `data/` - raw and processed datasets

## Prerequisites

- Python 3.10+ (project currently runs on 3.13/3.14 as well)
- Internet access for NASA FIRMS download in `download_fires.py`
- Required weather NetCDF files in `data/weather_datasets/`:
  - `total_precipitation_0_daily-mean.nc`
  - `2m_temperature_0_daily-mean.nc`
  - `2m_dewpoint_temperature_stream-oper_daily-mean.nc`

## Setup

From the project root:

```powershell
cd <path-to-repo>\wildfire_prediction
pip install -r requirements.txt
```

Optional (recommended): use a virtual environment/conda environment before installing dependencies.

## Run The Full Pipeline

From the project root:

```powershell
$env:PYTHONPATH = (Get-Location).Path
python src\main\main.py
```

The pipeline runs:
1. Download fires (`src/download/download_fires.py`)
2. Build weather CSV from NetCDF (`src/download/download_weather.py`)
3. Build features/labels (`src/preprocess/build_features.py`)
4. Train model (`src/model/train.py`)
5. Evaluate model (`src/model/evaluate.py`)

## Run Individual Steps

From the project root:

```powershell
$env:PYTHONPATH = (Get-Location).Path
python -c "import src.download.download_fires as m; m.main()"
python -c "import src.download.download_weather as m; m.main()"
python -c "import src.preprocess.build_features as m; m.main()"
python -c "import src.model.train as m; m.main()"
python -c "import src.model.evaluate as m; m.main()"
```

## Outputs

- `data/raw/fires.csv`
- `data/raw/weather.csv`
- `data/processed/dataset.csv`
- `data/processed/model.pt`

## Troubleshooting

- `ModuleNotFoundError: No module named 'src'`
  - Run from project root and set `PYTHONPATH` as shown above.
- `Cannot save file into a non-existent directory`
  - Make sure you are running the commands from project root.
- Missing package errors (`xarray`, `netCDF4`, etc.)
  - Re-run `pip install -r requirements.txt`.
