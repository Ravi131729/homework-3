import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load your favorite image
image_path = r'C:\Users\vvrav\OneDrive\Pictures\mountain.jfif' # Replace with the path to your image
original_image = cv2.imread(image_path)

# Apply the bilateral filter
bilateral_filtered_image = cv2.bilateralFilter(original_image, d=9, sigmaColor=75, sigmaSpace=75)

# Convert BGR to RGB for matplotlib visualization
original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
bilateral_filtered_image_rgb = cv2.cvtColor(bilateral_filtered_image, cv2.COLOR_BGR2RGB)

# Plot the original and filtered images using matplotlib
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.title('Original Image')
plt.imshow(original_image_rgb)
plt.axis('off')

plt.subplot(122)
plt.title('Bilateral Filtered Image')
plt.imshow(bilateral_filtered_image_rgb)
plt.axis('off')

plt.tight_layout()
plt.show()


