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

# Apply Gaussian Blur
blur = cv2.GaussianBlur(image, (15, 15), 0)

# Add labels
cv2.putText(image, "Original Image", (150, 35),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.putText(blur, "Gaussian Blur", (150, 35),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Display images side by side
combined = np.hstack((image, blur))

# Create resizable window
cv2.namedWindow("Original vs Gaussian Blur", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original vs Gaussian Blur", 1200, 500)

# Show output
cv2.imshow("Original vs Gaussian Blur", combined)

# Save output image
cv2.imwrite("gaussian_blur_output.jpg", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()