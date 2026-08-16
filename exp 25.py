import cv2

# Load the image
img = cv2.imread("berry.jpg")

if img is None:
    print("Image not found!")
    exit()

# Load pre-trained MobileNet SSD model
net = cv2.dnn.readNetFromCaffe(
    r"C:\Users\Siva Polam\Downloads\files\cv\MobileNetSSD_deploy.prototxt",
    r"C:\Users\Siva Polam\Downloads\files\cv\MobileNetSSD_deploy.caffemodel"
)

# Object classes
classes = [
    "background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
    "dog", "horse", "motorbike", "person", "pottedplant",
    "sheep", "sofa", "train", "tvmonitor"
]

# Create input blob
blob = cv2.dnn.blobFromImage(
    cv2.resize(img, (300, 300)),
    0.007843,
    (300, 300),
    127.5
)

net.setInput(blob)
detections = net.forward()

# Process detections
found = False

for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]

    if confidence > 0.3:
        class_id = int(detections[0, 0, i, 1])
        label = classes[class_id]

        # Display detected objects
        print("Detected:", label)

        # Watch is not included in MobileNet SSD classes
        if label == "watch":
            found = True

if found:
    print("Watch detected!")
else:
    print("Watch not detected by the general model.")

cv2.imshow("Input Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()