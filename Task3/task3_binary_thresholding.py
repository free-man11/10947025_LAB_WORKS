# Task 3: Manual binary thresholding question
pixel_value = 180
threshold = 150

new_pixel_value = 255 if pixel_value > threshold else 0
print(f"New pixel value after thresholding: {new_pixel_value}")
