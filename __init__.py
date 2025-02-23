from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import cv2

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

@app.route("/", methods=["POST"])
def members():
    data = request.get_json()
    return {"Members": ["Member1", "Member2", "Member3"]}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/upload-image', methods=['POST'])
def upload_image():
    '''if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Return a success message with the file path
        return jsonify({"message": f"Image uploaded successfully! File saved at {file_path}"})
    
    return jsonify({"error": "Invalid file format"}), 400'''

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    print("files ->")
    print(request.files)    
    file = request.files["image"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Load the image for processing
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return jsonify({"error": "Invalid image file"}), 400

    # Perform analysis (dummy response for now)
    analysis_result = {"message": "Image processed successfully!"}

    return jsonify(analysis_result)


#@app.route("/members")
#def members():
    #return {"Members": ["Member1", "Member2", "Member3"]}

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(host="0.0.0.0", port=8000, debug=True)
