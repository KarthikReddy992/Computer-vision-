import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread(r"C:\Users\Siva Polam\Downloads\files\cv\berry.jpg")

# Check image
if image is None:
    print("Image not found! Check the file path.")
    exit()

# Kernel
kernel = np.ones((5,5), np.uint8)

# Erode
eroded = cv2.erode(image, kernel, iterations=1)

# Display
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(eroded, cv2.COLOR_BGR2RGB))
plt.title("Eroded")
plt.axis("off")

plt.show()