"""
Comprehensive Guide: Indexing and Slicing in NumPy
==================================================
NumPy arrays allow powerful ways to access, modify, and analyze data using indexing and slicing. These techniques are essential for data science, machine learning, image processing, and scientific computing.

This guide covers:
- Basic indexing
- Slicing
- Advanced indexing
- Real-world examples
"""

import numpy as np

# 1. Basic Indexing
# =================
# Accessing individual elements by their position (zero-based)
arr = np.array([10, 20, 30, 40, 50])
first = arr[0]  # 10
last = arr[-1]  # 50
middle = arr[2]  # 30

# 2D array indexing
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
center = matrix[1, 1]  # 5
corner = matrix[2, 2]  # 9

# 2. Slicing
# ==========
# Extracting subarrays using start:stop:step
sub = arr[1:4]  # [20, 30, 40]
step_slice = arr[::2]  # [10, 30, 50] (every 2nd element)
reverse = arr[::-1]  # [50, 40, 30, 20, 10]

# 2D slicing
row_slice = matrix[1, :]  # [4, 5, 6] (entire 2nd row)
col_slice = matrix[:, 0]  # [1, 4, 7] (entire 1st column)
block = matrix[0:2, 1:3]  # [[2, 3], [5, 6]]

# 3. Advanced Indexing
# ====================
# Using lists/arrays of indices, boolean masks
indices = [0, 2, 4]
selected = arr[indices]  # [10, 30, 50]

mask = arr > 25
filtered = arr[mask]  # [30, 40, 50]

# 2D advanced indexing
rows = np.array([0, 2])
cols = np.array([1, 2])
selected_elements = matrix[rows, cols]  # [2, 9]

# Real-World Example 1: Image Cropping
# ------------------------------------
# Suppose 'img' is a grayscale image (2D array)
img = np.arange(100).reshape(10, 10)  # Simulated 10x10 image
crop = img[2:8, 3:7]  # Crop region (rows 2-7, cols 3-6)

# Real-World Example 2: Time Series Analysis
# ------------------------------------------
# Extract last 7 days from a month of sales data
sales = np.random.randint(100, 200, size=30)
last_week = sales[-7:]

# Real-World Example 3: Data Cleaning
# -----------------------------------
# Remove outliers (values > 180)

cleaned = sales[sales <= 180]

# Real-World Example 4: Selecting Features in ML
# ---------------------------------------------
# Select columns 1 and 3 from a dataset
features = np.random.rand(5, 4)  # 5 samples, 4 features
selected_features = features[:, [0, 2]]

# Real-World Example 5: Social Media Analytics
# --------------------------------------------
# Extract posts with >100 likes
likes = np.array([50, 120, 90, 200, 130])
popular_posts = likes[likes > 100]  # [120, 200, 130]

# Summary Tips:
# - Indexing: arr[i], arr[i, j]
# - Slicing: arr[start:stop:step], arr[:, col], arr[row, :]
# - Advanced: arr[list_of_indices], arr[mask]
# - Real-world: cropping images, filtering data, selecting features
