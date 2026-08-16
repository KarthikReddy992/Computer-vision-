import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the image
img = cv2.imread("berry.jpg")

# Check if image is loaded
if img is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a kernel
kernel = np.ones((5,5), np.uint8)

# Apply Morphological Opening
opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

# Display results
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(gray, cmap='gray')
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(opening, cmap='gray')
plt.title("Opening Operation")
plt.axis("off")

plt.tight_layout()
plt.show()