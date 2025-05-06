#!/bin/bash

mkdir -p ~/.streamlit
cp secrets.toml ~/.streamlit/

export TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata/

streamlit run app.py --server.port=10000 --server.enableCORS=false

