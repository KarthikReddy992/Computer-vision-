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

# Get image dimensions
h, w = img.shape[:2]

# Four source points (corners of the image)
pts1 = np.float32([
    [50, 50],
    [450, 50],
    [50, 450],
    [450, 450]
])

# Four destination points (perspective effect)
pts2 = np.float32([
    [0, 0],
    [500, 80],
    [80, 500],
    [500, 500]
])

# Compute Perspective Transformation Matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply Perspective Transformation
perspective = cv2.warpPerspective(img, matrix, (500, 500))

# Combine Original and Output images side by side
combined = np.hstack((img, perspective))

# Create a resizable window
cv2.namedWindow("Original Image          Perspective Transformation", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original Image          Perspective Transformation", 1200, 600)

# Display the images
cv2.imshow("Original Image          Perspective Transformation", combined)

# Save the output
cv2.imwrite("Perspective_Transformation_Output.jpg", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()