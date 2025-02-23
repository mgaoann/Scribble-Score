import { useState } from "react";

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
                body: formData
            });
            const data = await response.json();
            setResponse(data.message);
        } catch (error) {
            console.error("Error uploading image:", error);
        }
    };

    return (
        <div>
            <input type="file" accept="image/*" onChange={handleImageChange} />
            <button onClick={handleUpload}>Upload</button>
            {response && <p>{response}</p>}
        </div>
    )
};

export default ImageUploader;