from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="data")

trainer.setTrainConfig(object_names_array=["in"], batch_size=2, num_experiments=5)

trainer.trainModel()