import subprocess
import sys

steps = [
    'C:://Users//andra//Desktop//Projects//wildfire_prediction//src//download//download_fires.py',
    'C:://Users//andra//Desktop//Projects//wildfire_prediction//src//download//download_weather.py',
    'C:://Users//andra//Desktop//Projects//wildfire_prediction//src//download//download_ndvi.py',
    'C:://Users//andra//Desktop//Projects//wildfire_prediction//src//preprocess//build_features.py',
    'C:://Users//andra//Desktop//Projects//wildfire_prediction//src//models//train.py',
    'C:://Users//andra//Desktop//Projects//wildfire_prediction//src//models//evaluate.py'
]

for step in steps:
    result = subprocess.run([sys.executable, step])
    if result.returncode != 0:
        raise RuntimeError(f'Pipeline failed at {step} with error:')