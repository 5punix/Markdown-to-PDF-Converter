from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import os
import uuid
import logging

from md_top_pdf_converter import convert_md_to_pdf

app = Flask(__name__)
app.secret_key = "D771EB84E51C1F34FC47F28EAF4E4"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

UPLOAD_FOLDER = os.path.join(app.root_path, "uploads")
OUTPUT_FOLDER = os.path.join(app.root_path, "outputs")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

ALLOWED_MD_EXTENSIONS = {'md'}
ALLOWED_CSS_EXTENSIONS = {'css'}

def allowed_file(filename, allowed_extensions):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in allowed_extensions

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        md_file = request.files.get('markdown_file')

        if md_file is None or md_file.filename == '':
            flash('No Markdown file selected.', 'error')
            return redirect(url_for('index'))

        if not allowed_file(md_file.filename, ALLOWED_MD_EXTENSIONS):
            flash('Invalid Markdown file extension. Please upload a .md file.', 'error')
            return redirect(url_for('index'))

        unique_md_filename = str(uuid.uuid4()) + "_" + md_file.filename
        md_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_md_filename)
        md_file.save(md_path)
        logging.info(f"Uploaded markdown: {md_path}")
        
        css_path = None
        css_file = request.files.get('css_file')
        
        if css_file and css_file.filename != '':
            if allowed_file(css_file.filename, ALLOWED_CSS_EXTENSIONS):
                unique_css_filename = str(uuid.uuid4()) + "_" + css_file.filename
                css_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_css_filename)
                css_file.save(css_path)
                logging.info(f"Uploaded CSS: {css_path}")
            else:
                flash('Invalid CSS file extension. Please upload a .css file.', 'warning')
        
        output_pdf_name = os.path.splitext(unique_md_filename)[0] + ".pdf"
        output_pdf_path = os.path.join(app.config['OUTPUT_FOLDER'], output_pdf_name)
        
        try:
            convert_md_to_pdf(md_path, output_pdf_path, css_file_path=css_path)
            logging.info(f"Successfully converted {md_path} to {output_pdf_path}")
            
            return send_file(output_pdf_path, as_attachment=True, download_name=output_pdf_name)
        
        except FileNotFoundError as fnfe:
            flash(f"Error: A required file was not found. {fnfe}", 'error')
            logging.error(f"FileNotFoundError during conversion: {fnfe}")
        except Exception as e:
            flash(f"An unexpected error occurred during conversion: {e}", 'error')
            logging.error(f"Unexpected error during conversion: {e}", exc_info=True)
        finally:
            if os.path.exists(md_path):
                os.remove(md_path)
                logging.info(f"Cleaned up {md_path}")
            if css_path and os.path.exists(css_path):
                os.remove(css_path)
                logging.info(f"Cleaned up {css_path}")
        
        return redirect(url_for('index')) 

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)