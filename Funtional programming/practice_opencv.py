"""Practica con modulo OpenCV"""

import cv2


port = "554"
ip_address = "192.168.0.6"
# username = "callemdz"
username = "luismdz36"
password = "Luismdz36"
url_1080p = f"rtsp://{username}:{password}@{ip_address}:{port}/stream1"
url_480p = f"rtsp://{username}:{password}@{ip_address}:{port}/stream2"
# camara calle

cap = cv2.VideoCapture(url_1080p)
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imwrite('img3.png', frame)
cap.release()
