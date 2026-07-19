import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("berry image.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Resize image
image = cv2.resize(image, (600, 450))

# Convert BGR to RGB (for correct display in matplotlib)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Create figure
plt.figure(figsize=(12,5))

# Display Original Image
plt.subplot(1,2,1)
plt.imshow(rgb)
plt.title("Original Image")
plt.axis("off")

# Display Color Histogram
plt.subplot(1,2,2)

colors = ('b', 'g', 'r')
for i, color in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [256], [0,256])
    plt.plot(hist, color=color)

plt.title("Color Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.xlim([0,256])

plt.tight_layout()
plt.show()