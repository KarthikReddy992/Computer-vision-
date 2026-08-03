import cv2
import numpy as np

# Read the image
img = cv2.imread("berry image.jpg")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Enlarge the image for better visibility
img = cv2.resize(img, (500, 500))

# Get image dimensions
rows, cols = img.shape[:2]

# Define three points from the original image
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

# Define corresponding points in the output image
pts2 = np.float32([[20, 80], [250, 50], [100, 250]])

# Compute the Affine Transformation matrix
M = cv2.getAffineTransform(pts1, pts2)

# Apply the Affine Transformation
affine = cv2.warpAffine(img, M, (cols, rows))

# Combine original and transformed images side by side
combined = np.hstack((img, affine))

# Create a resizable window
cv2.namedWindow("Original Image      Affine Transformed Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original Image      Affine Transformed Image", 1200, 600)

# Display the combined image
cv2.imshow("Original Image      Affine Transformed Image", combined)

# Save the output
cv2.imwrite("Affine_Transformation_Output.jpg", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()