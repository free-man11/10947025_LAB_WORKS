# Task 2: Convert to HSV and LAB and plot histogram
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Save images
cv2.imwrite("photo_hsv.jpg", hsv)
cv2.imwrite("photo_lab.jpg", lab)
cv2.imwrite("photo_grayscale.jpg", gray)

# Display converted images
plt.figure(figsize=(15,4))
plt.subplot(1,3,1)
plt.title("Grayscale")
plt.imshow(gray, cmap='gray')
plt.axis("off")

plt.subplot(1,3,2)
plt.title("HSV")
plt.imshow(cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB))
plt.axis("off")

plt.subplot(1,3,3)
plt.title("LAB")
plt.imshow(cv2.cvtColor(lab, cv2.COLOR_LAB2RGB))
plt.axis("off")
plt.show()

# Plot histogram of grayscale image
plt.figure()
plt.title("Grayscale Histogram")
plt.hist(gray.ravel(), bins=256, range=[0,256])
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.show()
