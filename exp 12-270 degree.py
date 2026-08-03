import cv2

# Read the input image
img = cv2.imread("berry image.jpg")

# Check if the image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Enlarge the image (3 times)
large_img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

# 270° clockwise along the Y-axis (horizontal flip)
rotated = cv2.flip(large_img, 1)

# Create resizable windows
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("270 Degree Rotation Along Y-Axis", cv2.WINDOW_NORMAL)

# Set large window size
cv2.resizeWindow("Original Image", 900, 700)
cv2.resizeWindow("270 Degree Rotation Along Y-Axis", 900, 700)

# Display images
cv2.imshow("Original Image", large_img)
cv2.imshow("270 Degree Rotation Along Y-Axis", rotated)

# Save the output
cv2.imwrite("rotated_270_y_axis.jpg", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()