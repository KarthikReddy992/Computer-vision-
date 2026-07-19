import cv2
import numpy as np

# Read the image
image = cv2.imread("berry image.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Resize image for better display
image = cv2.resize(image, (600, 450))

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Histogram Equalization
equalized = cv2.equalizeHist(gray)

# Convert grayscale images to BGR for side-by-side display
gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
equalized_bgr = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)

# Add labels
cv2.putText(gray_bgr, "Original Gray Image", (110, 35),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.putText(equalized_bgr, "Histogram Equalized", (90, 35),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Combine images side by side
combined = np.hstack((gray_bgr, equalized_bgr))

# Create resizable window
cv2.namedWindow("Histogram Equalization", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Histogram Equalization", 1200, 500)

# Display output
cv2.imshow("Histogram Equalization", combined)

# Save output
cv2.imwrite("histogram_equalization_output.jpg", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()