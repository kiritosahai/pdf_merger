📄 pdf_merger

A lightweight and user-friendly web application for merging and splitting PDF files.

🔗 Live Demo

👉 https://pdf-merge-split.onrender.com/

🎯 Purpose

The purpose of this project is to provide a simple, fast, and accessible tool that allows users to:

Merge multiple PDF files into one

Split a single PDF into separate pages

Use these features directly in a browser without installing extra software

The app is designed with a clean interface, smooth navigation, mobile-friendly layout, and efficient backend processing.

🚀 Features
📌 Merge PDFs

Upload multiple PDF files

Combine them into one document

Instant download

📌 Split PDFs

Upload one PDF

Split into individual pages

Download pages individually or as a ZIP file

📌 UI / UX

Simple and clean design

Fully responsive on mobile, tablet, and desktop

Easy navigation

📌 File Handling

Temporary file storage

Automatic cleanup after processing

🛠️ Tech Stack
Frontend

HTML5

CSS3

JavaScript

Backend

Flask (Python)

PyPDF2

Zipfile

Deployment

Render (cloud hosting)

📂 Project Structure
/templates
    ├── index.html       # Merge page
    ├── split.html       # Split page
app.py                   # Backend logic
temp_files/              # Temporary PDF storage
README.md

▶️ Run Locally
1️⃣ Install dependencies:
pip install flask pypdf2

2️⃣ Run the server:
python app.py

3️⃣ Open in browser:
http://localhost:5000

🌐 Live Project

👉 https://pdf-merge-split.onrender.com/

👥 Team Members
Name	Enrollment No.
Yashica Shah	11024210230
Kushagra Sahai	11024210204
Kishlay Kaushal	11024210222
