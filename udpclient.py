import cv2
import socket
import numpy as np

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific IP address and port
client_address = ('127.0.0.1', 5005)
sock.bind(client_address)

while True:
    # Receive data from the socket
    data, address = sock.recvfrom(4096)

    # Create a numpy array from the bytes
    nparr = np.frombuffer(data, np.uint8)

    # Decode image from the array
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Display the image
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture
cv2.destroyAllWindows()
