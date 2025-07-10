import streamlit as st
import cv2
from utils.detector import detect_emotion
from utils.database import fetch_logs, init_db
import pandas as pd
import sys
import os

print("Current working directory:", os.getcwd())
print("Files in current dir:", os.listdir())

from utils.detector import detect_emotion


st.set_page_config(page_title="Emotion Recognition", layout="wide")
st.title("🎭 Real-Time Emotion Recognition")

init_db()

run = st.checkbox('Start Webcam')
FRAME_WINDOW = st.image([])

cap = None
if run:
    cap = cv2.VideoCapture(0)

while run and cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame, emotions = detect_emotion(frame)
    FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

if cap:
    cap.release()

st.subheader("📊 Emotion Logs")
logs = fetch_logs(20)
df = pd.DataFrame(logs, columns=["ID", "Timestamp", "Emotion"])
st.dataframe(df)


# import os, sys

# print("Current Directory:", os.getcwd())
# print("Folder contains:", os.listdir())
# print("utils folder exists:", os.path.exists("utils"))
# print("detector.py exists:", os.path.exists("utils/detector.py"))

# sys.path.append(os.getcwd())
# from utils.detector import detect_emotion

# print("Success:", detect_emotion("test"))
