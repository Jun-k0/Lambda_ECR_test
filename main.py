import json
from fer import Video
from fer import FER
import cv2


def my_handler(event, context):
    print("Hello, lambda")
    try:
        print(event)
        face_detector = FER(mtcnn=True)
    except Exception as e:
        print("error -> " + str(e))
        return {
            'statusCode': 500,
            'body': json.dumps("error")
        }
    return {
        'statusCode': 200,
        'body': json.dumps("Hello")
    }
