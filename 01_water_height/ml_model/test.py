from imageai.Detection.Custom import CustomObjectDetection
import os
from datetime import date

########### MODEL SET UP
MODEL = "yolov3_data_mAP-0.44211_epoch-4"

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(f"data/models/{MODEL}.pt")
detector.setJsonPath("data/json/data_yolov3_detection_config.json")
detector.loadModel()

########### IMAGE SET UP
# path to images to test
dir = "data/validation/images"
num = 1
test_dir = f"manual_tests/{MODEL}-{str(date.today())}"

# make the new directory for the output
i = 1
while (os.path.exists(test_dir)):
    test_dir = f"manual_tests/{MODEL}-{i}-{str(date.today())}"
    i += 1
os.mkdir(test_dir) 

for filename in os.listdir(dir):
    # concat the full path together
    file = os.path.join(dir, filename)

    # if valid path, do detection
    if os.path.isfile(file):
        detections = detector.detectObjectsFromImage(input_image=file, output_image_path=f"{test_dir}/detected-{num}.jpg")
        for detection in detections:
            print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
        num += 1