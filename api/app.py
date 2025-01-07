from flask import Flask, request, jsonify
import joblib
import numpy as np
from skimage.io import imread
from skimage.transform import resize

# Inisialisasi Flask
app = Flask(__name__)

# Muat model
model = joblib.load("model.pkl")

# Parameter gambar
IMAGE_SIZE = (128, 128)  # Sesuaikan dengan ukuran input model Anda

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Periksa apakah file gambar diunggah
        if 'file' not in request.files:
            return jsonify({"error": "File gambar tidak ditemukan!"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "Nama file kosong!"}), 400

        # Baca gambar
        image = imread(file)
        image_resized = resize(image, IMAGE_SIZE, anti_aliasing=True)

        # Ubah gambar menjadi array 1D (flatten)
        features = image_resized.flatten().reshape(1, -1)

        # Prediksi menggunakan model
        prediction = model.predict(features)
        label = "Asli" if prediction[0] == 1 else "Palsu"

        return jsonify({"prediction": label})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
