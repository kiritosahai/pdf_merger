📄 pdf_merger

A lightweight and user-friendly web application for merging and splitting PDF files.
Live Demo:
👉 https://pdf-merge-split.onrender.com/

🎯 Purpose

The goal of this project is to provide a simple, fast, and accessible tool that allows users to:

Merge multiple PDF files into one.

Split a single PDF into separate pages.

Perform these tasks easily from a browser without installing any software.

The application is designed with a clean interface, mobile responsiveness, and quick processing using an efficient backend.

🚀 Features
📌 Merge PDFs

Upload multiple PDF files

Combine them into a single merged document

Instant download

📌 Split PDFs

Upload one PDF

Split it into individual pages

Download pages individually or as a ZIP file

📌 UI / UX

Clean and simple design

Fully responsive (works on mobile, tablet, and desktop)

Smooth navigation between Merge and Split pages

📌 File Handling

Temporary file storage

Automatic cleanup after operations

🛠️ Tech Stack
Frontend

HTML5

CSS3

JavaScript (for file handling on UI)

Backend

Flask (Python framework)

PyPDF2 (for PDF merging and splitting)

Zipfile (for packaging multiple pages)

Deployment

Render (for hosting the full-stack application)

📂 Project Structure
/templates
    ├── index.html      # Merge PDF page
    ├── split.html      # Split PDF page
app.py                  # Main backend logic
temp_files/             # Temporary storage for PDF processing
README.md

▶️ Run Locally

Install dependencies:

pip install flask pypdf2


Run the server:

python app.py


Open in browser:

http://localhost:5000

🌐 Live Project

👉 https://pdf-merge-split.onrender.com/

👥 Team Members
Name	Enrollment No.
Yashica Shah	11024210230
Kushagra Sahai	11024210204
Kishlay Kaushal	11024210222
