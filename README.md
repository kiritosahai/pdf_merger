📄 pdf_merger

Hello! This project is called pdf_merger — a simple and user-friendly web application made to merge and split PDF files online.

Live Demo:
👉 https://pdf-merge-split.onrender.com/

🎯 Purpose

The purpose of this project is to help users manage PDF documents easily without installing any software.
Our application lets users:

Merge multiple PDFs into one combined file

Split a single PDF into separate pages

Use everything directly in a browser

It is designed to be simple, fast, and accessible, with a friendly interface and smooth performance on both computer and mobile screens.

🚀 Features
✳️ Merge PDFs

Select multiple PDF files

Merge them into a single document

Download instantly

✳️ Split PDFs

Select one PDF

Split it into individual pages

Download pages separately or as a ZIP file

✳️ User Experience

Clean and neat interface

Easy navigation between pages

Fully responsive design

✳️ Smart File Handling

Uses temporary storage

Files are cleaned up automatically after processing

🛠️ Tech Stack

We used a modern and lightweight tech stack:

Layer	Technology
Frontend	HTML5, CSS3, JavaScript
Backend	Flask (Python), PyPDF2, Zipfile
Hosting	Render
📂 Project Structure
/templates
    ├── index.html       # Merge page
    ├── split.html       # Split page
app.py                   # Backend logic
temp_files/              # Temporary storage for PDFs
README.md

▶️ Run Locally

Install required packages:

pip install flask pypdf2


Run the project:

python app.py


Then open in browser:

http://localhost:5000

🌐 Live Preview

Try it here:
👉 https://pdf-merge-split.onrender.com/

👥 Team Members
Name	Enrollment No.
Yashica Shah	11024210230
Kushagra Sahai	11024210204
Kishlay Kaushal	11024210222

✨ Thank you for checking out our project!
We hope this tool makes working with PDFs easier and faster!
