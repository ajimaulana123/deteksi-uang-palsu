# Gunakan base image Python
FROM python:3.9-slim

# Atur working directory
WORKDIR /app

# Salin semua file ke dalam container
COPY . /app

# Install dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Ekspos port
EXPOSE 5000

# Jalankan aplikasi
CMD ["python", "app.py"]
