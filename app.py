from flask import Flask, render_template, request, send_file
import PyPDF2
import os
import uuid
import zipfile

app = Flask(__name__)

TEMP_FOLDER = "temp_files"
os.makedirs(TEMP_FOLDER, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html') 


@app.route('/merge', methods=['POST'])
def merge_pdfs():
    files = request.files.getlist("pdfs")

    if not files:
        return "No PDFs uploaded.", 400

    pdfmerger = PyPDF2.PdfMerger()
    saved_paths = []

    for file in files:
        temp_path = os.path.join(TEMP_FOLDER, f"{uuid.uuid4()}_{file.filename}")
        file.save(temp_path)
        saved_paths.append(temp_path)

    for p in saved_paths:
        pdfmerger.append(p)

    output_path = os.path.join(TEMP_FOLDER, f"merged_{uuid.uuid4()}.pdf")
    pdfmerger.write(output_path)
    pdfmerger.close()


    for p in saved_paths:
        os.remove(p)

    return send_file(output_path, as_attachment=True)


@app.route('/split_page')
def split_page():
    return render_template('split.html')


@app.route('/split', methods=['POST'])
def split_pdf():
    file = request.files.get("pdf")
    split_type = request.form.get("split_type")

    if not file:
        return "No PDF uploaded.", 400

    temp_path = os.path.join(TEMP_FOLDER, f"{uuid.uuid4()}_{file.filename}")
    file.save(temp_path)

    reader = PyPDF2.PdfReader(temp_path)
    outputs = []

    if split_type == "all":
        for i, page in enumerate(reader.pages):
            writer = PyPDF2.PdfWriter()
            writer.add_page(page)

            out_path = os.path.join(TEMP_FOLDER, f"page_{i+1}_{uuid.uuid4()}.pdf")
            with open(out_path, "wb") as f:
                writer.write(f)

            outputs.append(out_path)

    elif split_type == "range":
        start = int(request.form.get("start")) - 1
        end = int(request.form.get("end"))

        writer = PyPDF2.PdfWriter()
        for i in range(start, end):
            writer.add_page(reader.pages[i])

        out_path = os.path.join(TEMP_FOLDER, f"split_range_{uuid.uuid4()}.pdf")
        with open(out_path, "wb") as f:
            writer.write(f)

        outputs.append(out_path)

    os.remove(temp_path)

    if len(outputs) == 1:
        return send_file(outputs[0], as_attachment=True)

    zip_path = os.path.join(TEMP_FOLDER, f"split_{uuid.uuid4()}.zip")
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for p in outputs:
            zipf.write(p, arcname=os.path.basename(p))
            os.remove(p)

    return send_file(zip_path, as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)
