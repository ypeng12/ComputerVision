# CMSC426

# Homework 1 - Line Fitting with Outlier Rejection Techniques

## Overview
This repository contains my solutions to Homework 1 for the course CMSC426. The assignment was designed to test the understanding of linear least squares techniques and outlier rejection methods, with a specific focus on RANSAC. The objective was to fit the best possible line to two-dimensional data points, taking into account different noise levels.

## Data Visualization
The 2D points data, provided in `.mat` files, was visualized using Matplotlib in Python. Three datasets with varying levels of noise were examined.

## Eigenvalues and Covariance Matrix
The first task was to visualize the geometric interpretation of eigenvalues and the covariance matrix. This involved calculating the covariance matrices and eigenvectors for each dataset and plotting them using the quiver function in Matplotlib.

## Outlier Rejection Techniques
Two outlier rejection techniques were explored:
1. Ridge Regression
2. RANSAC

Each technique was applied to fit a line to the datasets, and the mean squared error (MSE) was calculated to evaluate the fit's quality.

## Results and Analysis
Ridge Regression consistently yielded lower MSE values across all datasets, making it the preferred method for this particular assignment. The analysis included a discussion on the robustness of Ridge Regression and its effectiveness in handling outliers.

## Limitations of Outlier Rejection Techniques
The limitations of RANSAC and Ridge Regression were discussed, highlighting the sensitivity of RANSAC to hyperparameters and the general nature of Ridge Regression not being specifically tailored for outlier rejection.

## Conclusion
The homework provided a practical understanding of line fitting in the presence of noise and the application of outlier rejection techniques. Ridge Regression emerged as the optimal technique for the given datasets due to its robustness and lower MSE values.

---

# CMSC426 Project 1: Color Segmentation using GMM

## Introduction

In the quest to enhance robotic capabilities, this project focuses on training Nao robots for RoboCup soccer competitions. The primary goal is to enable Nao to detect a soccer ball and estimate its distance with precision.

## Project Overview

The project involves two key phases:
1. **Color Segmentation using Gaussian Mixture Model (GMM):** Leveraging the power of GMM, we aim to accurately segment the orange soccer ball from a series of images.
2. **Ball Distance Estimation:** With the ball detected, the next step is to determine how far it is from the robot, which is critical for planning the kick.

## Implementation Highlights

- **Color Space and Segmentation:** We utilized the RGB color space for segmenting the orange soccer ball.
- **Algorithm Development:** Custom Python code was developed to cluster the orange ball using both a Single Gaussian and a GMM.
- **Distance Estimation:** A novel approach was adopted to estimate the ball's distance from the robot based on the segmented area.

## Challenges and Solutions

During the course of this project, we encountered and overcame several challenges, such as dealing with similar color distributions that could confuse the segmentation process. The algorithm was fine-tuned to distinguish between the soccer ball and other objects with a semblance of color similarity.

## Results

Our algorithm successfully segments the soccer ball and estimates its distance across various test images, demonstrating the robustness of the GMM approach over a single Gaussian model.

## Concluding Thoughts

This project serves as a stepping stone towards developing sophisticated vision systems for autonomous robots, pushing the boundaries of what they can perceive and act upon in their environment.

---



*For detailed code, results, and figures, please refer to the respective Jupyter Notebook files in this repository.*
