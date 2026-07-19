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

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges using Canny
edges = cv2.Canny(blur, 100, 200)

# Convert edges to BGR for side-by-side display
edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

# Add labels
cv2.putText(image, "Original Image", (150, 35),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.putText(edges_bgr, "Canny Edge Detection", (90, 35),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Combine images side by side
combined = np.hstack((image, edges_bgr))

# Create a resizable window
cv2.namedWindow("Original vs Canny Edge Detection", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original vs Canny Edge Detection", 1200, 500)

# Display the result
cv2.imshow("Original vs Canny Edge Detection", combined)

# Save the output image
cv2.imwrite("canny_output.jpg", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()