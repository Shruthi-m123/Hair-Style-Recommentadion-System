# User_Points.py

import face_recognition
import numpy as np

def user_points(img_path):
    input_image = face_recognition.load_image_file(img_path)
    face_landmarks = face_recognition.face_landmarks(input_image)
    ans = []
    landmarkn = face_landmarks[0].get('nose_bridge')
    x, y = landmarkn[0]
    landmarkc = face_landmarks[0].get('chin')
    x1, y1 = landmarkc[8]
    height = np.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
    ans.append(height)
    x2, y2 = landmarkc[0]
    x3, y3 = landmarkc[16]
    width = np.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    ans.append(width)
    x4, y4 = landmarkc[4]
    x5, y5 = landmarkc[12]
    jaw_width = np.sqrt((x4 - x5) ** 2 + (y4 - y5) ** 2)
    ans.append(jaw_width)
    x6, y6 = landmarkc[6]
    x7, y7 = landmarkc[10]
    chin = np.sqrt((x6 - x7) ** 2 + (y6 - y7) ** 2)
    ans.append(chin)
    landmarkl = face_landmarks[0].get('left_eyebrow')
    x8, y8 = landmarkl[0]
    x9, y9 = landmarkc[5]
    side = np.sqrt((x8 - x9) ** 2 + (y8 - y9) ** 2)
    ans.append(side)
    ans.append(height / width)
    ans.append(height / jaw_width)
    ans.append(height / chin)
    ans.append(height / side)
    ans.append(width / jaw_width)
    ans.append(width / chin)
    ans.append(width / side)
    ans.append(jaw_width / chin)
    ans.append(jaw_width / side)
    ans.append(chin / side)
    return ans
