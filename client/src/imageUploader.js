import { useState } from "react";
//import './styles2.css';

const ImageUploader = () => {
    const [selectedImage, setSelectedImage] = useState(null);
    const [response, setResponse] = useState("");

    const handleImageChange = (event) => {
        setSelectedImage(event.target.files[0]);
    }

    const handleUpload = async () => {
        if (!selectedImage) {
            return;
        }

        const formData = new FormData();
        formData.append("image", selectedImage);

        try {
            const response = await fetch("http://localhost:8000/upload-image", {
                method: "POST",
                body: formData,
            });
            const data = await response.json();
            //setResponse(data.message);
            setResponse({
                message: data.message,
                handwriting_score: data.handwriting_score,
                alignment_suggestion: data.alignment_suggestion,
                spacing_suggestion: data.spacing_suggestion
            });
        } catch (error) {
            console.error("Error uploading image:", error);
        }
    };

    return (
        <div>
            {/*{selectedImage && (
                <div>
                    <img
                        src={URL.createObjectURL(selectedImage)} // Preview image before upload
                        alt="Selected Preview"
                        style={{ maxWidth: "100%", maxHeight: "300px", marginBottom: "10px" }}
                    />
                </div>
            )}*/}
            <input type="file" accept="image/*" onChange={handleImageChange} />
            <button onClick={handleUpload}>Upload</button>
            {/*{response && <p>{response}</p>}*/}
            {response && (
                <div>
                    <p><strong>Message:</strong> {response.message}</p>
                    <p><strong>Handwriting Score:</strong> {response.handwriting_score}</p>
                    <p><strong>Alignment Suggestion:</strong> {response.alignment_suggestion}</p>
                    <p><strong>Spacing Suggestion:</strong> {response.spacing_suggestion}</p>
                </div>
            )}

        </div>
    )
};

export default ImageUploader;