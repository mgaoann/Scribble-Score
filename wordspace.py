import cv2
import numpy as np
import matplotlib.pyplot as plt
from sobel import sobel, normal, curve

def detect_word_spaces(img, threshold=10):
    """
    Detects spaces between words in a handwritten text image and checks for uniformity.
    Groups letters into words based on the spaces between them, ignoring punctuation and small disconnected components.
    
    img: grayscale image of handwritten text.
    threshold: acceptable deviation in space sizes.
    return: list of detected space widths, average space, standard deviation.
    """
    # Convert to binary
    _, binary = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
    
    # Morphological closing to connect nearby letters horizontally and vertically
    letter_widths = []
    letter_heights = []
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        letter_widths.append(w)
        letter_heights.append(h)
    
    if letter_widths:
        avg_letter_width = int(np.median(letter_widths))
    else:
        avg_letter_width = 10
    
    if letter_heights:
        avg_letter_height = int(np.median(letter_heights))
    else:
        avg_letter_height = 10

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (avg_letter_width, 5))
    closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

    # Morphological closing vertically to merge dotted letters
    kernel_vert = cv2.getStructuringElement(cv2.MORPH_RECT, (avg_letter_height, 10))
    closed = cv2.morphologyEx(closed, cv2.MORPH_CLOSE, kernel_vert)

    # Find contours (connected components of text)
    #contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find contours again after closing
    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    bounding_boxes = [cv2.boundingRect(cnt) for cnt in contours if cv2.contourArea(cnt) > 15]
    bounding_boxes.sort(key=lambda b: b[0]) # Sort bounding boxes by x-coordinate (left to right)
    
    # Compute spaces between words
    spaces = [bounding_boxes[i+1][0] - (bounding_boxes[i][0] + bounding_boxes[i][2])
              for i in range(len(bounding_boxes)-1)]
    
    if len(spaces) == 0:
        return [], 0, 0  # No spaces found
    
    # Compute average space width and standard deviation
    avg_space = np.mean(spaces)
    std_dev = np.std(spaces)
    
    return spaces, avg_space, std_dev, bounding_boxes, contours

def rate_spacing_uniformity(image):
    """
    Evaluates the uniformity of word spacing in handwriting.
    
    image: grayscale image of handwritten text.
    return: a score and an improvement suggestion.
    """
    spaces, avg_space, std_dev, bounding_boxes, contours = detect_word_spaces(image)
    
    if not spaces:
        return 100, "No word spacing issues detected.", bounding_boxes, contours
    
    # Normalize score between 0 and 100
    score = max(0, min(100, 100 - (std_dev / (avg_space + 1e-5)) * 100))
    
    suggestion = "Word spacing is consistent. Keep up the good work!" if score > 80 else \
                 "Try to maintain more uniform spacing between words for better readability."
    
    return score, suggestion, bounding_boxes, contours

def show_contours(image, bounding_boxes, contours):
    """
    Displays the image with detected contours and bounding boxes drawn.

    image: original image.
    bounding_boxes: list of bounding boxes of detected words.
    contours: list of contours of detected words.
    """
    image_copy = image.copy()
    cv2.drawContours(image_copy, contours, -1, (0, 255, 0), 2)
    
    for (x, y, w, h) in bounding_boxes:
        cv2.rectangle(image_copy, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    plt.figure(figsize=(10, 6))
    plt.imshow(cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB))
    plt.title("Detected Word Spaces and Contours")
    plt.axis("off")
    plt.show()

# Load the image
image_path = input("Enter the image file path: ")
image = cv2.imread(image_path)
if image is None:
    print("Error: The provided file is not a valid image or does not exist.")
    exit()
else:
    print("Image loaded successfully!")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Image to grayscale
spacing_score, spacing_suggestion, bounding_boxes, contours = rate_spacing_uniformity(gray) # Evaluate spacing uniformity

# Output the results
print(f"Word Spacing Score: {spacing_score:.2f}")
print(f"Spacing Improvement Suggestion: {spacing_suggestion}")
show_contours(image, bounding_boxes, contours)