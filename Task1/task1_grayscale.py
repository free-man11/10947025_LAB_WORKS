# Task 1: Load and convert to grayscale
import cv2
from matplotlib import pyplot as plt

# Upload an image
from google.colab import files
uploaded = files.upload()

# Load the image
img_path = list(uploaded.keys())[0]
image = cv2.imread(img_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save grayscale image
cv2.imwrite("photo_gray.jpg", gray)

# Display both images
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Grayscale")
plt.imshow(gray, cmap='gray')
plt.axis("off")
plt.show()
