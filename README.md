# CMSC426

# CMSC426 Homework 1 - Line Fitting with Outlier Rejection Techniques

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

*For detailed code, results, and figures, please refer to the respective Jupyter Notebook files in this repository.*
