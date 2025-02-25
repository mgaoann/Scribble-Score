# ✏️ Scribble Score

Scribble Score is a web application that checks handwriting consistency and offers feedback. Designed for kids, the user interface and dyslexia-friendly fonts make learning fun and accessible. This project was initially developed for [Boilermake XII](https://boilermake-xii.devpost.com/?_gl=1*qs70q6*_gcl_au*MjEzNTkxODYxLjE3Mzg4MTMxMzM.*_ga*MTg4MzQyOTQ3Ny4xNzM4ODEzMTMz*_ga_0YHJK3Y10M*MTc0MDUxOTUwNi4xMS4wLjE3NDA1MTk1NjYuMC4wLjA.).

Scribble Score scans a JPG or PNG and processes it to read the handwriting, then rate the legibility of handwriting based on parameters such as consistent spacing and straightness of lines.

### Built With:
- React - created the user interface for uploading handwriting images and displaying feedback
- Flask - managed API requests, processed images, and handled communication between front and backend
- OpenCV - preprocessed handwriting images including thresholding and contour detection
- Tesseract OCR - extracted text from handwriting samples
- NumPy - handled matrix operations and other numerical computations
- Matplotlib - generated visualizations

## Contributors
- Angela Qian - Developed the backend, implemented handwriting slant analysis and scoring, and contributed to UI design and implementation
- Maggie Gao - Developed the backend, implemented handwriting spacing analysis and scoring, contributed to UI design, and helped integrated the frontend and backend 
- Linda Xu - Developed the frontend and integrated it with the backend
- William Ruan - Developed the frontend

## Acknowledgements
Special thanks to the mentors at Boilermake XII for the guidance and support, the judges for their valuable feedback, and the Boilermake organizer team for fostering a collaborative environment.
