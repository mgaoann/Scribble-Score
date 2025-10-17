# ✏️ Scribble Score

Scribble Score is a web application that checks handwriting consistency and offers feedback. Designed for kids, the user interface and dyslexia-friendly fonts make learning fun and accessible. This project was initially developed for [Boilermake XII](https://boilermake-xii.devpost.com/?_gl=1*qs70q6*_gcl_au*MjEzNTkxODYxLjE3Mzg4MTMxMzM.*_ga*MTg4MzQyOTQ3Ny4xNzM4ODEzMTMz*_ga_0YHJK3Y10M*MTc0MDUxOTUwNi4xMS4wLjE3NDA1MTk1NjYuMC4wLjA.).

Scribble Score scans a JPG or PNG and processes it to read the handwriting, then rates the legibility of handwriting based on parameters such as consistent spacing and straightness of lines.

### Built With:
- React - created the user interface for uploading handwriting images and displaying feedback
- Flask - managed API requests, processed images, and handled communication between front and backend
- OpenCV - preprocessed handwriting images including thresholding and contour detection
- NumPy - handled matrix operations and other numerical computations
- Matplotlib - generated visualizations

## Running the Project Locally

Follow these steps to run both the backend (Flask) and frontend (Vite React) locally.

### 1. Clone the Repository

```bash
git clone https://github.com/mgaoann/Scribble-Score
```

---

### 2. Set Up the Backend
Create and activate a virtual environment

```bash
cd backend
python -m venv venv
```
#### Activate the virtual environment
On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

#### Install dependencies
```bash
pip install
```

#### Run the Flask server
```bash
python __init__.py
```

---

### 3. Set Up the Frontend
Open a new terminal and navigate to the frontend directory:
```bash
cd client-vite
```

#### Install dependencies
```bash
npm install
```

#### Run the development server
```bash
npm run dev
```

---

### 4. Access the Application
Open your browser and navigate to http://localhost:5173

---

## Future Plans and Improvements
- Improve UI/UX - Further styling and polishing the page
- Expanded Handwriting Criteria - Developing new metrics for evaluating handwriting
- Enhanced Data Visualization - Adding more graphical representations of handwriting analysis
- Deployment - Hosting the project online

## Contributors
- [Angela Qian](https://github.com/angelazqian) - Developed the backend, implemented handwriting slant analysis and scoring, and contributed to UI design and implementation
- [Maggie Gao](https://github.com/mgaoann) - Developed the backend, implemented handwriting spacing analysis and scoring, contributed to UI design, and helped integrated the frontend and backend 
- [Linda Xu](https://github.com/lindarxu) - Developed the frontend and integrated it with the backend
- [William Ruan](https://github.com/willruan) - Developed the frontend

## Acknowledgements
Special thanks to the mentors at Boilermake XII for the guidance and support, the judges for their valuable feedback, and the Boilermake organizer team for fostering a collaborative environment.
