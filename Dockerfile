# Dockerfile

# 1. Base image
FROM python:3.11-slim

# 2. Install system dependencies (including Tesseract OCR)
RUN apt-get update \
 && apt-get install -y \
       tesseract-ocr \
       libsm6 libxext6 libxrender-dev \
       libjpeg-dev zlib1g-dev libpng-dev libtiff-dev libfreetype6-dev \
 && rm -rf /var/lib/apt/lists/*

# 3. Set working directory
WORKDIR /app

# 4. Copy project files
COPY . /app

# 5. Upgrade pip and install Python dependencies
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# 6. Expose the port Streamlit uses (10000 matches your start command)
EXPOSE 10000

# 7. Launch the app
CMD ["streamlit", "run", "app.py", "--server.port=10000", "--server.enableCORS=false"]
