import cv2
import socket

# Initialize video capture
cap = cv2.VideoCapture(0)

# Set video capture properties
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Create UDP socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Encode frame as JPEG
    success, jpeg = cv2.imencode('.jpg', frame)

    # Send JPEG over UDP
    sock.sendto(jpeg.tobytes(), (UDP_IP, UDP_PORT))

# Release video capture
cap.release()
