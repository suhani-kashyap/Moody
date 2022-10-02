import cv2
import pywhatkit
from deepface import DeepFace
import random
from tkinter import *
import time

HAPPY_SONGS = ['https://www.youtube.com/watch?v=jv-pYB0Qw9A','https://www.youtube.com/watch?v=wWPY-Qi0aVQ']
SAD_SONGS = ['https://www.youtube.com/watch?v=RW0OZi8W7Gs','https://www.youtube.com/watch?v=74UkuOXZSEM']
NEUTRAL_SONGS = ['https://www.youtube.com/watch?v=1M6Yp5-lPM4','https://www.youtube.com/watch?v=7NhVtH9CS7U']
ANGRY_SONGS=['https://www.youtube.com/watch?v=XJxSWkPhblE','https://www.youtube.com/watch?v=FAIr1vDqxnM']
DISGUST_SONGS=['https://www.youtube.com/watch?v=pQHQnrmYuhk&list=PLcWxP8I-VJlxatxjwpLLM0fi7dwk-VNL6&index=5']
FEAR_SONGS=['https://www.youtube.com/watch?v=iyEUvUcMHgE','https://www.youtube.com/watch?v=xXhEz3hqlQE']
SURPRISE_SONGS=['https://www.youtube.com/watch?v=0H6n1aK0ZSo','https://www.youtube.com/watch?v=dQw4w9WgXcQ']
FONT_NAME="Courier"
enforce_detection=False
mood = ""
def capture_image():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Camera")

    img_counter = 0

    while img_counter==0:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
        cv2.imshow("Camera", frame)

        k = cv2.waitKey(1)
        if k%256 == 32:
            # SPACE pressed
            img_name = "image_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()
    title.config(text="Image Captured!")
    capture_img_button.config(text="Predict mood",command=predict_mood)


def predict_mood():
    title.config(text="Predicting Mood...")
    capture_img_button.config(text="")
    img=cv2.imread('image_0.jpg')
    predictions = DeepFace.analyze(img)
    mood_predic = predictions['dominant_emotion']
    global mood
    mood = mood_predic
    title.config(text="Mood: "+mood)
    capture_img_button.config(text="Play Music",command=play_music)

def play_music():
    global mood
    if mood=="happy":
        url = random.choice(HAPPY_SONGS)
    elif mood=="sad":
        url = random.choice(SAD_SONGS)
    elif mood=="neutral":
        url = random.choice(NEUTRAL_SONGS)
    elif mood=="angry":
        url = random.choice(ANGRY_SONGS)
    elif mood=="disgust":
        url = random.choice(DISGUST_SONGS)
    elif mood=="fear":
        url = random.choice(FEAR_SONGS)
    else:
        url = random.choice(SURPRISE_SONGS)
    pywhatkit.playonyt(url)


BLUE="#94B49F"
L_BLUE="#CEE5D0"
L_PINK="#FCF8E8"
PINK="#ECB390"
WHITE="#F5EFE6"
################################# GUI #############################################
window=Tk()
window.title("Moody - Play Music")
window.config(padx=100, pady=100,bg=L_BLUE)
#
title = Label(window,text="Moody")
title.config(font=(FONT_NAME,40,"bold"),bg=L_BLUE)
title.grid(column=0, row=0,columnspan=2)
#

capture_img_button=Button(window,text="Capture Image", highlightthickness=0, command=capture_image)
capture_img_button.config(bg=PINK,font=(FONT_NAME,30,"bold"),fg=WHITE)
capture_img_button.grid(column=0, row=1,columnspan=2)

window.mainloop()
#
