import cv2
import socket
import numpy as np

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific IP address and port
server_address = ('127.0.0.1', 5005)
sock.bind(server_address)

# Initialize video capture
cap = cv2.VideoCapture(0)

# Set video capture properties
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print('Server started, streaming video...')

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Encode frame as JPEG
    success, jpeg = cv2.imencode('.jpg', frame)

    # Send JPEG over UDP
    sock.sendto(jpeg.tobytes(), ('127.0.0.1', 5005))

# Release video capture
cap.release()
