import ImagePuller
import time
import Roboflow
from twilio.rest import Client
import cv2


def imagePuller():
    try:
        cap = cv2.VideoCapture(192.168.1.100:8080/video)

        if not cap.isOpened():
            raise Exception("Error: Unable to access the camera.")

        ret, frame = cap.read()

        if not ret:
            raise Exception("Error: Unable to capture a frame from the camera.")

        image_filename = "captured_image.jpg"
        cv2.imwrite(image_filename, frame)

        cap.release()

        return image_filename

    except Exception as e:
        return str(e)

account_sid = '3K9pR7sF2tT6uX8wA1'
auth_token = 'aB3dE1G8iK2mN5pQ7rT9'
client = Client(account_sid, auth_token)

rf = Roboflow(api_key="c702fd4b704e484c83bd4b4747772017")
project = rf.workspace().project("cow-disease-classifier")
model = project.version(1).model

while True:
    image = ImagePuller()
    response = model.predict(image, confidence = 70, overlap = 30).json()
    for pred in response["predictions"]:
        if pred['class'] in ['snot_on_cow', 'neck_drooping', 'isolated_from_herd']:
            message = client.messages.create(
            body="CAUTION: There is a cow that is sick on your field. Type of illness "+ pred['class'],
            media_url= image;
            from_='+17147878999', 
            to='+13124567345'      
        )   
    time.sleep(20)



