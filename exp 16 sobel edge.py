import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("berry.jpg")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel filter
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Convert to absolute values
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Combine Sobel X and Sobel Y
sobel = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

# Display outputs like the sample
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(sobel_x, cmap='gray')
plt.title("Sobel_X", fontsize=18)
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(sobel_y, cmap='gray')
plt.title("Sobel_Y", fontsize=18)
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(sobel, cmap='gray')
plt.title("Sobel_Combination", fontsize=18)
plt.axis("off")

plt.tight_layout()
plt.show()