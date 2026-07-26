import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread(r"C:\Users\Siva Polam\Downloads\files\cv\berry.jpg")

# Check if image is loaded
if image is None:
    print("Image not found! Check the file path.")
    exit()

# Rotate image 90 degrees clockwise
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Display images
plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB))
plt.title("90° Clockwise Rotation")
plt.axis("off")

plt.show()