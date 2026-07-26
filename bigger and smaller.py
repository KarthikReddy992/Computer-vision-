import cv2
import matplotlib.pyplot as plt

# Read image
image = cv2.imread(r"C:\Users\Siva Polam\Downloads\files\cv\berry.jpg")

# Check if image is loaded
if image is None:
    print("Image not found! Check the file path.")
    exit()

# Scale up (2 times bigger)
bigger = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Scale down (half size)
smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Display images
plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(cv2.cvtColor(bigger, cv2.COLOR_BGR2RGB))
plt.title("Scaled Up (2x)")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(cv2.cvtColor(smaller, cv2.COLOR_BGR2RGB))
plt.title("Scaled Down (0.5x)")
plt.axis("off")

plt.show()