# -*- coding: utf-8 -*-
"""Python script.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fWc0ZXklsyxmpGzqquYhCU3XEkPzR5o8
"""

!pip install pymupdf pytesseract pdf2image

!apt-get install tesseract-ocr

!pip install pytesseract

import csv
import os
import zipfile
import tempfile
import shutil
from pdf2image import convert_from_path
import fitz  # PyMuPDF
import pytesseract

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(pdf_file)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    doc.close()
    return text

def extract_text_from_image(image_path):
    return pytesseract.image_to_string(image_path)

def extract_key_value_pairs(text):
    # Add your logic to extract key-value pairs from the text
    # This will depend on the specific structure of your invoices
    # For demonstration purposes, let's assume a simple key-value pair format
    pairs = []
    lines = text.split('\n')
    for line in lines:
        if ':' in line:
            key, value = map(str.strip, line.split(':', 1))
            pairs.append((key, value))
    return pairs

def save_to_csv(data, csv_path):
    with open(csv_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)

def process_files(zip_path, output_folder_path):
    # Create a temporary directory to extract the contents
    with tempfile.TemporaryDirectory() as temp_dir:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        for file_name in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, file_name)

            if file_name.lower().endswith('.pdf'):
                text = extract_text_from_pdf(file_path)
            elif file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                text = extract_text_from_image(file_path)
            else:
                continue

            key_value_pairs = extract_key_value_pairs(text)
            output_csv_path = os.path.join(output_folder_path, os.path.splitext(file_name)[0] + '_output.csv')
            save_to_csv(key_value_pairs, output_csv_path)

if __name__ == "__main__":
    # Use correct file path
    zip_file_path = '/content/Sample Files.zip'

    # Replace 'output_folder' with the desired output folder path
    output_folder_path = 'output_folder'

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder_path, exist_ok=True)

    process_files(zip_file_path, output_folder_path)