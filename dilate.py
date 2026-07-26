import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread(r"C:\Users\Siva Polam\Downloads\files\cv\berry.jpg")

# Check if image is loaded
if image is None:
    print("Image not found! Check the file path.")
    exit()

# Create a 5x5 kernel
kernel = np.ones((5,5), np.uint8)

# Apply dilation
dilated = cv2.dilate(image, kernel, iterations=1)

# Display images
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(dilated, cv2.COLOR_BGR2RGB))
plt.title("Dilated Image")
plt.axis("off")

plt.show()