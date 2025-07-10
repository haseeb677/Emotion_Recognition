import cv2
import numpy as np
from keras.models import load_model
from utils.database import log_emotion

# Labels for the emotion classes
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load your trained emotion detection model
model = load_model(r"C:\Users\Haseeb Ali\OneDrive\Documents\Emotion_Recognition\model\emotion_model.h5")

def detect_emotion(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    emotions_detected = []

    for (x, y, w, h) in faces:
        roi = gray[y:y+h, x:x+w]
        roi = cv2.resize(roi, (48, 48)) / 255.0
        roi = np.expand_dims(roi, axis=0)
        roi = np.expand_dims(roi, axis=-1)

        prediction = model.predict(roi)
        emotion = emotion_labels[np.argmax(prediction)]
        emotions_detected.append(emotion)

        log_emotion(emotion)

        # Draw rectangle and label on the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    # Return both the updated frame and the list of emotions
    return frame, emotions_detected
