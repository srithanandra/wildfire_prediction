import download.download_fires, download.download_weather, model.train, model.evaluate, preprocess.build_features

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