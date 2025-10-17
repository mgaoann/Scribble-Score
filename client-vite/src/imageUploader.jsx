import { useState } from "react";
import axios from "axios";
import './styles.css'; // optional, if you have styles for uploader

const ImageUploader = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [response, setResponse] = useState(null);

  const handleImageChange = (event) => {
    setSelectedImage(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!selectedImage) return;

    const formData = new FormData();
    formData.append("image", selectedImage);

    try {
      // Use relative URL for Vite proxy
      const res = await axios.post("/upload-image", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setResponse({
        message: res.data.message,
        handwriting_score: res.data.handwriting_score,
        alignment_suggestion: res.data.alignment_suggestion,
        spacing_suggestion: res.data.spacing_suggestion,
      });
    } catch (error) {
      console.error("Error uploading image:", error);
      setResponse({
        message: "Error uploading image.",
        handwriting_score: "N/A",
        alignment_suggestion: "N/A",
        spacing_suggestion: "N/A",
      });
    }
  };

  return (
    <div className="image-uploader">
      <input type="file" accept="image/*" onChange={handleImageChange} />
      <button onClick={handleUpload}>Upload</button>

      {response && (
        <div className="upload-response">
          <p><strong>Message:</strong> {response.message}</p>
          <p><strong>Handwriting Score:</strong> {response.handwriting_score}</p>
          <p><strong>Alignment Suggestion:</strong> {response.alignment_suggestion}</p>
          <p><strong>Spacing Suggestion:</strong> {response.spacing_suggestion}</p>
        </div>
      )}
    </div>
  );
};

export default ImageUploader;