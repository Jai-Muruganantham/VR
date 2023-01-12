import socket
from PIL import Image

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific IP address and port
server_address = ('127.0.0.1', 5005)
sock.bind(server_address)

print('Listening for incoming JPEG images on %s:%s' % server_address)

while True:
    # Receive data from the socket
    data, address = sock.recvfrom(4096)
    print('Received %s bytes from %s' % (len(data), address))
    # Create a file-like buffer to receive JPEG data
    image_buffer = io.BytesIO(data)
    # Open image file
    image = Image.open(image_buffer)
    # Do something with the image
    image.show()
