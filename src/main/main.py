import src.download.download_fires as download_fires
import src.download.download_weather as download_weather
import src.model.train as train
import src.model.evaluate as evaluate
import src.preprocess.build_features as build_features
from time import time

start_time = time()

download_fires.main()
print('Downloaded fires')
download_weather.main()
print('Downloaded weather')
build_features.main()
print('Built features')
train.main()
print('Trained model')
evaluate.main()
print('COMPLETED PROCESS')

end_time = time()
print(f'TOTAL TIME: {(end_time-start_time)//60} minutes and {(end_time-start_time)%60} seconds')