import cv2
import numpy as np

# Read the input image
img = cv2.imread("berry image.jpg")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Resize image for better visibility
img = cv2.resize(img, (500, 500))

# Create a copy for output
output = img.copy()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Apply Harris Corner Detection
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# Dilate the result to make corners more visible
dst = cv2.dilate(dst, None)

# Mark detected corners in red
output[dst > 0.01 * dst.max()] = [0, 0, 255]

# Combine original and output images side by side
combined = np.hstack((img, output))

# Create a resizable window
cv2.namedWindow("Original Image      Harris Corner Detection", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original Image      Harris Corner Detection", 1200, 600)

# Display the result
cv2.imshow("Original Image      Harris Corner Detection", combined)

# Save the output
cv2.imwrite("Harris_Corner_Output.jpg", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()