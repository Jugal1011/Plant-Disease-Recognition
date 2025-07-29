from flask import Flask, request, jsonify, render_template
import numpy as np
import cv2
from tensorflow.keras.models import load_model
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load the pre-trained model
model = load_model('./model/plant-disease-recognition.hdf5')

# Define your classes (replace these with your actual class labels)
class_labels = {
    0: "Healthy",
    1: "Powdery",
    2: "Rust"
}

def preprocess_image(image):
    # Resize and normalize image
    resized_image = cv2.resize(image, (80, 80))
    normalized_image = resized_image / 255.0
    return normalized_image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        filename = secure_filename(file.filename)
        file_bytes = np.frombuffer(file.read(), np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        preprocessed_image = preprocess_image(image)
        prediction = model.predict(np.array([preprocessed_image]))
        predicted_class = np.argmax(prediction, axis=1)[0]

        class_label = class_labels.get(predicted_class, "Unknown")
        return jsonify({'prediction': class_label})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # Use Flask 2.3 style app run
    app.run(debug=True)
