from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="data")

trainer.setTrainConfig(object_names_array=["in"], batch_size=5, num_experiments=20)

trainer.trainModel()

# batch 5 and 20 experiments took 12m 32s