import cv2

# Read the input image
image = cv2.imread("berry image.jpg")

# Check if the image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Rotate 180° along the y-axis (horizontal flip)
rotated = cv2.flip(image, 1)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("180 Degree Rotation Along Y-Axis", rotated)

# Save the output image
cv2.imwrite("rotated_y_axis.jpg", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()