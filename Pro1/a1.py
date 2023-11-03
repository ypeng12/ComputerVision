import cv2
import numpy as np
from scipy.stats import multivariate_normal
from skimage.measure import label, regionprops
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import os

# TODO: Import all python packages you need

# File paths and variables
train_images_dir = '/content/train_images/'

images = []
for filename in os.listdir(train_images_dir):
  if filename[-4:]=='.jpg':
    images.append(mpimg.imread(os.path.join(train_images_dir, filename)))
train_files = ["106", "114", "121", "137", "144", "152", "160", "168", "176", "192", "200", "208", "216", "223", "231", "248", "256", "264", "280", "68", "76", "91"]




s = 0
mean = np.zeros(3)
dists = []
areas = []

# TODO: Read in training images
for file_num in train_files:
    mask_file = f"data/{file_num}.mat"  # Replace with your actual mask files
    image_file = f"train_images/{file_num}.jpg"
    
    # Load mask (replace this line with actual mask loading logic)
    # mask = load_mat_file(mask_file)
    
    img = cv2.imread(image_file)
    
    if img is None:
        print(f"Image {image_file} could not be read.")
        continue
    
    area = 0
    R, G, B = img[:,:,2], img[:,:,1], img[:,:,0]
    
    # TODO: Iterate over training images to extract orange pixels using masks
    # Here I assume `mask` is a binary mask where 1 indicates orange pixels.
    for i in range(R.shape[0]):
        for j in range(R.shape[1]):
            if mask[i, j]:
                area += 1
                mean += [R[i, j], G[i, j], B[i, j]]

    s += area
    dist = int(file_num)
    dists.append(dist)
    areas.append(area)

mean = mean / s

# TODO: Compute mean and covariance using MLE(Maximum Likelihood Estimation)
cova = np.zeros((3, 3))
for file_num in train_files:
    mask_file = f"data/{file_num}.mat"
    image_file = f"train_images/{file_num}.jpg"
    
    # Load mask
    # mask = load_mat_file(mask_file)
    
    img = cv2.imread(image_file)
    R, G, B = img[:,:,2], img[:,:,1], img[:,:,0]
    
    for i in range(R.shape[0]):
        for j in range(R.shape[1]):
            if mask[i, j]:
                x = np.array([R[i, j], G[i, j], B[i, j]], dtype=float)
                cova += np.outer(x - mean, x - mean) / s

det_cova = np.linalg.det(cova)

# TODO: Compute PDF(Probability Density Function) of single gaussian model
pdf = multivariate_normal(mean=mean, cov=cova)

# Load test image
test_img = cv2.imread(test_file)
if test_img is None:
    print(f"Test image {test_file} could not be read.")
    exit()

R, G, B = test_img[:,:,2], test_img[:,:,1], test_img[:,:,0]
heatmap = np.zeros(R.shape)

# TODO: Send test images into algorithm to detect orange ball
for i in range(R.shape[0]):
    for j in range(R.shape[1]):
        x = np.array([R[i, j], G[i, j], B[i, j]], dtype=float)
        like = 1e6 * 2 / np.sqrt((2 * np.pi)**3 * det_cova) * np.exp(-0.5 * np.dot(np.dot((x - mean).T, np.linalg.inv(cova)), x - mean))
        heatmap[i, j] = like

binary_heatmap = heatmap > 1

# TODO: Set parameters (threshold, prior)
label_img = label(binary_heatmap)
props = regionprops(label_img)

max_area = 0
for prop in props:
    local_area = np.pi * prop['major_axis_length'] * prop['minor_axis_length'] / 4
    if local_area > max_area:
        max_area = local_area

# Fit model and predict
f = interp1d(areas, dists, kind='linear')
print(round(f(max_area)))

# Display for report
plt.imshow(binary_heatmap, cmap='gray')
plt.show()
