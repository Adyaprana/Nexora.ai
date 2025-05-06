#!/bin/bash

# Step 1: Set up Streamlit secrets
mkdir -p ~/.streamlit
cp secrets.toml ~/.streamlit/

# Step 2: Export Tesseract OCR environment variable
export TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata/

# Step 3: Start Streamlit
streamlit run app.py --server.port=10000 --server.enableCORS=false
