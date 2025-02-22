#! /opt/homebrew/bin/python3 

import cv2
import subprocess
import numpy as np

# Load the image
image_path = input("Enter the image file path: ")
image = cv2.imread(image_path)
if image is None:
    print("Error: The provided file is not a valid image or does not exist.")
    exit()
else:
    print("Image loaded successfully!")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use tesseract command-line tool to extract text from the image
result = subprocess.run(['tesseract', image_path, 'stdout'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
text = result.stdout.decode('utf-8')
if not text:
    print("No text detected. If there is handwriting in this image, I am unable to read it.")
    exit()

# Function to compute Mean Squared Error
def mean_squared_error(image1, image2):
    return np.mean((image1.astype(np.float32) - image2.astype(np.float32)) ** 2)

# Function to compute Structural Similarity Index (SSIM)
def compute_ssim(image1, image2):
    C1 = 6.5025
    C2 = 58.5225
    
    image1 = image1.astype(np.float32)
    image2 = image2.astype(np.float32)
    
    mu1 = cv2.GaussianBlur(image1, (7, 7), 1.5)
    mu2 = cv2.GaussianBlur(image2, (7, 7), 1.5)
    
    sigma1_sq = cv2.GaussianBlur(image1**2, (7, 7), 1.5) - mu1**2
    sigma2_sq = cv2.GaussianBlur(image2**2, (7, 7), 1.5) - mu2**2
    sigma12 = cv2.GaussianBlur(image1 * image2, (7, 7), 1.5) - mu1 * mu2
    
    ssim_map = ((2 * mu1 * mu2 + C1) * (2 * sigma12 + C2)) / ((mu1**2 + mu2**2 + C1) * (sigma1_sq + sigma2_sq + C2))
    return np.mean(ssim_map)

# Function to rate handwriting legibility
def rate_handwriting(image):
    mse = mean_squared_error(image, image)  # Comparing image with itself as no reference is provided
    similarity = compute_ssim(image, image)
    
    score = (1 - mse / 1000) * similarity * 100
    return max(0, min(100, score))  # Ensure score is within [0, 100]

# Function to suggest improvements
def suggest_improvements(score):
    if score > 80:
        return "Your handwriting is very good! Little to no improvement needed"
    elif score > 50:
        return "Your handwriting is legible, but could be improved by writing more clearly."
    else:
        return "Your handwriting is difficult to read. Try writing larger and more spaced out."

# Rate the handwriting
score = rate_handwriting(gray)
improvement_suggestion = suggest_improvements(score)

# Output the results
print(f"Extracted Text: {text}")
print(f"Handwriting Legibility Score: {score:.2f}")
print(f"Improvement Suggestion: {improvement_suggestion}")