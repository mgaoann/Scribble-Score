#! /opt/homebrew/bin/python3 

import cv2
import subprocess
import numpy as np
from sobel import sobel, normal, curve
from bestfit import best_fit
from wordspace import detect_word_spaces, rate_spacing_uniformity

# def mean_squared_error(image1, image2):
#     return np.mean((image1.astype(np.float32) - image2.astype(np.float32)) ** 2)

# def compute_ssim(image1, image2):
#     C1 = 6.5025
#     C2 = 58.5225
    
#     image1 = image1.astype(np.float32)
#     image2 = image2.astype(np.float32)
    
#     mu1 = cv2.GaussianBlur(image1, (7, 7), 1.5)
#     mu2 = cv2.GaussianBlur(image2, (7, 7), 1.5)
    
#     sigma1_sq = cv2.GaussianBlur(image1**2, (7, 7), 1.5) - mu1**2
#     sigma2_sq = cv2.GaussianBlur(image2**2, (7, 7), 1.5) - mu2**2
#     sigma12 = cv2.GaussianBlur(image1 * image2, (7, 7), 1.5) - mu1 * mu2
    
#     ssim_map = ((2 * mu1 * mu2 + C1) * (2 * sigma12 + C2)) / ((mu1**2 + mu2**2 + C1) * (sigma1_sq + sigma2_sq + C2))
#     return np.mean(ssim_map)

def rate_handwriting(image):
    score = best_fit(image)
    #print(score)
    score = min((1 - score) * 120, 100)
    score = max(score, 0)
    return score

# suggest improvements
def vert_improvements(score):
    if score > 80:
        return "Little to no improvement needed"
    elif score > 50:
        return "Your letters and words are at inconsistent heights, try writing in a straighter line"
    else:
        return "Your letters are scattered at various heights, use lined paper as practice"



image_path = input("Enter the image file path: ")
image = cv2.imread(image_path)
if image is None:
    print("Error: The provided file is not a valid image or does not exist.")
    exit()
else:
    print("Image loaded successfully!")

# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
# Resize the image if its dimensions are larger than 400
height, width = gray.shape
if height > 400 or width > 400:
    scaling_factor = 400 / max(height, width)
    gray = cv2.resize(gray, (int(width * scaling_factor), int(height * scaling_factor)), interpolation=cv2.INTER_AREA)
sob = curve(sobel(gray))

#use tesseract to get text from img
result = subprocess.run(['tesseract', image_path, 'stdout'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
text = result.stdout.decode('utf-8')
if not text:
    print("No text detected. If there is handwriting in this image, I am unable to read it.")
# Rate the handwriting
score = rate_handwriting(sob)
vert_suggestion = vert_improvements(score)
spacing_score, spacing_suggestion, bounding_boxes, contours = rate_spacing_uniformity(gray) # Evaluate spacing uniformity
# print(score)
# print(spacing_score)
score += spacing_score - 100
# Output the results
if text:
    print(f"Extracted Text: {text}",end="")
print(f"Handwriting Legibility Score: {score:.2f}")
print(f"Alignment Improvement Suggestions: {vert_suggestion}")
print(f"Spacing Improvement Suggestion: {spacing_suggestion}")
