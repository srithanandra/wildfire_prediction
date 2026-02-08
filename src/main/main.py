import download.download_fires, download.download_weather, model.train, model.evaluate, preprocess.build_features
from time import time

start_time = time()

download.download_fires.main()
print('Downloaded fires')
#download.download_weather.main()
print('Downloaded weather')
preprocess.build_features.main()
print('Built features')
model.train.main()
print('Trained model')
model.evaluate.main()
print('COMPLETED PROCESS')

end_time = time()
print(f'TOTAL TIME: {(end_time-start_time)//60} minutes and {(end_time-start_time)%60} seconds')