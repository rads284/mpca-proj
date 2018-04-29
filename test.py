
import cv2
from cv2 import *

import os

import numpy as np
# import RPi.GPIO as GPIO
# import time
#
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(12, GPIO.OUT)
# p=GPIO.PWM(12, 50)

print("Now i m testing")
subjects = ["", "PR", "Elvis Presley","ramiz raja","Paro"]
def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);

    if (len(faces) == 0):
        return None, None

    (x, y, w, h) = faces[0]

    return gray[y:y+w, x:x+h], faces[0]

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainer.yml')
def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)


def predict(test_img):
    img = test_img.copy()

    face, rect = detect_face(img)
    if face==None:
        return('a',100)


    label, confidence = face_recognizer.predict(face)

    label_text = subjects[label]


    draw_rectangle(img, rect)
    draw_text(img, label_text, rect[0], rect[1]-5)

    return (label_text,confidence)

def testfun():
    print('test1')
    test_img1 = cv2.imread("test-data/test1.jpg")
    print('test2')
    test_img2 = cv2.imread("test-data/test2.jpg")
    print('test3')
    test_img3 = cv2.imread("test-data/test3.jpg")
    print('test4')
    test_img4 = cv2.imread("test-data/test4.jpg")
    print('test5')
    test_img5 = cv2.imread("test-data/test5.jpg")

    #perform a prediction
    print('predict1')
    pr1 = predict(test_img1)
    print('predict2')
    pr2 = predict(test_img2)
    print('predict3')
    pr3 = predict(test_img3)
    print('predict4')
    pr4 = predict(test_img4)
    print('predict5')
    pr5 = predict(test_img5)
    print("Prediction complete")

    conflist=[pr1[1],pr2[1],pr3[1],pr4[1],pr5[1]]
    print(conflist)
    flg=True
    for conf in conflist:
        if conf<20.5:
            flg=False
            print('servo opens')
            # p.start(2.5)
            # p.ChangeDutyCycle(7.5)
            # time.sleep(1)
            # p.ChangeDutyCycle(12.5)
            # time.sleep(5)
            # p.ChangeDutyCycle(2.5)
            # time.sleep(1)
            break

            # add servo confidence
    if flg:
        from mtest import mailit
        mailit()
        print('INTRUDER ALERT SENT')
testfun()
