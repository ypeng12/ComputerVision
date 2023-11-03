# TODO: Import all python packages you need
import cv2
import os
import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Initialize variables
orange_pixels_lab_list = []

# TODO: Read in training images
image_folder = '/content/train_images'  # Replace with your image folder path

# Check if the folder exists
if not os.path.exists(image_folder):
    print(f"The folder {image_folder} does not exist.")
else:
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]

    if len(image_files) == 0:
        print("No image files found in the directory.")
    else:
        # Display some training images
        num_images_to_show = 5
        for i, image_file in enumerate(image_files[:num_images_to_show]):
            image_path = os.path.join(image_folder, image_file)
            image = mpimg.imread(image_path)
            
            plt.subplot(1, num_images_to_show, i+1)
            plt.imshow(image)
            plt.axis("off")
            plt.title(f"Image {i+1}")

        plt.show()

        # TODO: Iterate over training images to extract orange pixels using masks
        for image_file in image_files:
            image_path = os.path.join(image_folder, image_file)
            image = cv2.imread(image_path)
            
            if image is None:
                print(f"Image {image_path} could not be read.")
                continue

            image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
            
            # Define color thresholds in LAB space
            l_min, l_max = 19.510, 91.394
            a_min, a_max = 14.923, 51.449
            b_min, b_max = 10.049, 46.717

            # Create mask based on thresholds
            mask = (image_lab[:,:,0] >= l_min) & (image_lab[:,:,0] <= l_max) & \
                   (image_lab[:,:,1] >= a_min) & (image_lab[:,:,1] <= a_max) & \
                   (image_lab[:,:,2] >= b_min) & (image_lab[:,:,2] <= b_max)
            
            orange_pixels_current = image_lab[mask]
            orange_pixels_lab_list.append(orange_pixels_current)

        # Combine orange pixels from all images
        if len(orange_pixels_lab_list) == 0:
            print("No orange pixels found.")
        else:
            orange_pixels_lab = np.vstack(orange_pixels_lab_list)

            # TODO: Compute mean and covariance using MLE
            mean_orange_lab = np.mean(orange_pixels_lab, axis=0)
            cov_orange_lab = np.cov(orange_pixels_lab.T)

            # TODO: Compute PDF of single Gaussian model
            pdf = multivariate_normal(mean=mean_orange_lab, cov=cov_orange_lab)

            # TODO: Set parameters (threshold, prior)
            threshold = 0.0001

            # TODO: Send test images into algorithm to detect orange ball
            test_image_path = 'test_image.jpg'  # Replace with your test image path
            test_image = cv2.imread(test_image_path)
            test_image_lab = cv2.cvtColor(test_image, cv2.COLOR_BGR2Lab)
            pdf_values = pdf.pdf(test_image_lab.reshape(-1, 3))
            mask_test = pdf_values > threshold
            mask_test = mask_test.reshape(test_image_lab.shape[:2])
            result_image = test_image * np.repeat(mask_test[:, :, np.newaxis], 3, axis=2)

            # Display result
            plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
            plt.axis('off')
            plt.show()
