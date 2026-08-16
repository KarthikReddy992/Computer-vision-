import cv2
import matplotlib.pyplot as plt

# Read the input image
img = cv2.imread("berry.jpg")

# Check whether image is loaded
if img is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel in X direction
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Apply Sobel in Y direction
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Convert to absolute values
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Combine Sobel X and Y
sobel = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

# Display images
plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(sobel_x, cmap='gray')
plt.title("Sobel_X")
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(sobel_y, cmap='gray')
plt.title("Sobel_Y")
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(sobel, cmap='gray')
plt.title("Sobel_Combination")
plt.axis('off')

plt.tight_layout()
plt.show()