# Uang Asli vs Palsu Detection API

## Deskripsi Proyek

API ini menggunakan model machine learning untuk mendeteksi apakah sebuah gambar uang adalah asli atau palsu. Model ini dilatih menggunakan dataset gambar uang asli dan menggunakan metode One-Class SVM untuk mendeteksi anomali (uang palsu).

## Fitur Utama

- **Prediksi Gambar Uang**: API menerima input berupa gambar uang dan memberikan hasil prediksi apakah uang tersebut asli atau palsu.
- **Model Machine Learning**: Menggunakan model One-Class SVM yang dilatih pada dataset uang asli.
- **Endpoint RESTful**: Mudah diintegrasikan dengan aplikasi lain melalui HTTP POST request.

## Teknologi yang Digunakan

- **Python**: Bahasa pemrograman utama.
- **Flask**: Framework untuk membangun API.
- **scikit-learn**: Untuk membangun dan menyimpan model machine learning.
- **scikit-image**: Untuk memproses gambar.
- **joblib**: Untuk menyimpan dan memuat model machine learning.

## Instalasi

### 1. Clone Repository

```bash
https://github.com/ajimaulana123/deteksi-uang-palsu.git
```

### 2. Buat Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Untuk Linux/Mac
venv\Scripts\activate   # Untuk Windows
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

### 4. Jalankan API

```bash
python3 app.py
```

## Endpoint

### **POST /predict**

- **Deskripsi**: Memprediksi apakah gambar uang yang diberikan asli atau palsu.
- **Input**: File gambar uang dalam format multipart/form-data.
- **Output**: JSON dengan prediksi.

#### Contoh Request

```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: multipart/form-data" \
-F "file=@path_to_image.jpg"
```

#### Contoh Response

```json
{
  "prediction": "Asli"
}
```

## Catatan Penting

1. Dataset hanya berisi uang asli. Model memprediksi uang palsu berdasarkan perbedaan ciri dari data uang asli.
2. API ini dirancang untuk dihosting di platform seperti Vercel.
3. Pastikan ukuran gambar sesuai dengan parameter input model.

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

