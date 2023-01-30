from imageai.Detection.Custom import CustomObjectDetection

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("data/models/yolov3_data_mAP-0.01970_epoch-3.pt")
detector.setJsonPath("data/json/data_yolov3_detection_config.json")
detector.loadModel()

detections = detector.detectObjectsFromImage(input_image="data/train/images/017e2bcc-in_15.jpg", output_image_path="holo1-detected.jpg")
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])