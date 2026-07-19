import cv2
import numpy as np

# Read the image
image = cv2.imread("berry image.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Resize original image (Width, Height)
image = cv2.resize(image, (600, 450))

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert grayscale to BGR (3 channels)
gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

# Put labels on images
cv2.putText(image, "Original Image", (150, 35),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.putText(gray_bgr, "Gray Scale Image", (120, 35),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Combine images side by side
combined = np.hstack((image, gray_bgr))

# Show a large window
cv2.namedWindow("Original vs Gray Scale", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original vs Gray Scale", 1200, 500)

cv2.imshow("Original vs Gray Scale", combined)

# Save output
cv2.imwrite("output_side_by_side.jpg", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()