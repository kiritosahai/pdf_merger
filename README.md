📄 **PDF Merger and Splitter**

A lightweight web application designed for merging and splitting PDF files quickly and easily.

🔗 **Live Demo**
👉 [https://pdf-merge-split.onrender.com/](https://pdf-merge-split.onrender.com/)

---

### Purpose

This project aims to provide a simple online tool that allows users to:

* Merge multiple PDF files into one document
* Split a PDF into separate pages
* Manage PDFs without installing any additional software

The interface is minimal, easy to use, and works well on both desktop and mobile devices.

---

### Features

#### **Merge PDFs**

* Upload multiple PDFs
* Combine into a single file
* Download instantly

#### **Split PDFs**

* Upload one PDF
* Automatically separate pages
* Download individual pages or a ZIP file

#### **User Interface**

* Clean layout
* Clear buttons and workflow
* Stable on different screen sizes

#### **File Handling**

* Temporary file storage only
* Automatic cleanup after processing

---

### Tech Stack

| Component | Technology                    |
| --------- | ----------------------------- |
| Frontend  | HTML5, CSS3, JavaScript       |
| Backend   | Python Flask, PyPDF2, Zipfile |
| Hosting   | Render                        |

---

### Project Structure

```
/templates
    ├── index.html
    ├── split.html
app.py
temp_files/
README.md
```

---

### How to Run Locally

1. Install dependencies:

```bash
pip install flask pypdf2
```

2. Start the application:

```bash
python app.py
```

3. Visit in browser:

```
http://localhost:5000
```

---

### Team Members

| Name            | Enrollment No. |
| --------------- | -------------- |
| Yashica Shah    | 11024210230    |
| Kushagra Sahai  | 11024210204    |
| Kishlay Kaushal | 11024210222    |

