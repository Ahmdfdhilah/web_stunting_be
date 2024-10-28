# Gunakan Python image sebagai base
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev

# Set working directory
WORKDIR /app/web_stunting_be

# Copy requirements file dan instal dependencies
COPY web_stunting_be/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY ./web_stunting_be /app/web_stunting_be

# Instal proyek lokal
RUN pip install -e .

# Expose port yang digunakan aplikasi
EXPOSE 6543

# Jalankan perintah untuk memulai aplikasi Pyramid
CMD ["pserve", "development.ini"]