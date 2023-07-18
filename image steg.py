# Import necessary libraries
import numpy as np
import cv2

# Load the 3D geometric image
image = cv2.imread('3d_geometric_image.png')

# Choose the secret message to hide in the image
message = "Hello, World!"

# Encode the secret message into a binary sequence
binary_message = ''.join(format(ord(i), '08b') for i in message)

# Determine the pixels to modify in the 3D image based on the binary sequence
pixels_to_modify = []
for i in range(len(binary_message)):
    x = np.random.randint(image.shape[0])
    y = np.random.randint(image.shape[1])
    z = np.random.randint(image.shape[2])
    pixels_to_modify.append((x, y, z))

# Modify the pixel values to hide the secret message
for i in range(len(pixels_to_modify)):
    x, y, z = pixels_to_modify[i]
    pixel_value = list(image[x, y, z])
    pixel_value[-1] = int(binary_message[i])
    image[x, y, z] = tuple(pixel_value)

# Save the steganographic image
cv2.imwrite('steganographic_image.png', image)
