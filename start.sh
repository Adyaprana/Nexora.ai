#!/bin/bash

# Step 1: Prepare Streamlit secrets
mkdir -p .streamlit
cp secrets.toml .streamlit/

# Step 2: Set Tesseract environment (for OCR to work on Render)
export TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata/

# Step 3: Start your Streamlit app
streamlit run app.py --server.port=10000 --server.enableCORS=false
