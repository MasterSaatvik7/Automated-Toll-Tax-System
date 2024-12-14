import cv2
from ultralytics import YOLO
import numpy as np
import pandas as pd
import pytesseract

def preprocess_image(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # Apply adaptive thresholding
    thresholded = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return thresholded

# Function to extract text from image
def extract_text(image):
    # Preprocess the image
    processed_image = preprocess_image(image)
    # Perform OCR using pytesseract with custom configuration
    custom_config = r'--oem 3 --psm 6'  # OCR Engine Mode: 3, Page Segmentation Mode: 6
    text = pytesseract.image_to_string(processed_image, config=custom_config)
    return text
# Load the model
model = YOLO('license_plate_detector.pt')

cap = cv2.VideoCapture('170609_A_Delhi_026.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference
    results = model(frame)[0]
    # Draw the bounding boxes
    for plate in results.boxes.data.tolist():
        x1, y1, x2, y2, score,class_id = plate
        frame_lp = frame[int(y1):int(y2), int(x1):int(x2)]
        try:
            text = extract_text(frame_lp)
            print(text)
            cv2.imshow('frame', frame_lp)
        except:
            cv2.imshow('frame', frame)

    #cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break