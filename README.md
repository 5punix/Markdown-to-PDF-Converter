# Markdown to PDF Converter

**Instant Markdown to PDF Conversion – sleek, simple, and brandable.**

This project offers a lean, web-based tool to quickly transform Markdown (`.md`) files into polished PDF documents. It's built with **Python (Flask)** and uses **WeasyPrint** for high-fidelity rendering, with support for optional custom CSS to ensure brand consistency.

---

## 🚀 Why This Matters for Your Business

- **Efficiency** – Streamlines document creation from Markdown, saving time and effort.  
- **Professionalism** – Converts internal notes or documentation into sleek, presentation-ready PDFs.  
- **Custom Branding** – Easily apply your company's unique styles with custom CSS.

---

## 🌐 Live Demo

👉 [Click here to try the live web app](https://markdown-to-pdf-converter.onrender.com)

_Experience it yourself – no setup required._

---

## 🛠️ Get Started Locally

Follow the steps below to set up the project on your local machine.

### ✅ Prerequisites

- Python `3.8+`  
- `pip` (Python package installer)  
- **GTK 3 Runtime** (for Windows users only): WeasyPrint relies on external C libraries.

> **Windows:**  
> Download and install GTK 3 from:  
> [GTK for Windows Runtime Installer Releases](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer)  
> Look for a file like: `gtk3-runtime-x.y.z-with-dependencies-installer.exe`

> **macOS / Linux:**  
> Use your package manager:  
> ```bash
> # macOS (with Homebrew)
> brew install cairo pango gdk-pixbuf
> 
> # Debian/Ubuntu
> sudo apt-get install build-essential python3-dev python3-pip python3-setuptools \
> python3-wheel libffi-dev libcairo2 libpango-1.0-0 libpangocairo-1.0-0 \
> libgdk-pixbuf2.0-0 libxml2-dev libxslt1-dev
> ```

---

## 🧭 Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/5punix/Markdown-to-PDF-Converter.git
cd md_to_pdf
```
### 2. Set Up a Virtual Environment
```
python -m venv venv
```
### 3. Activate the Virtual Environment

- Windows:
```
.\venv\Scripts\activate
```
- macOS/Linux:

```
source venv/bin/activate
```
### 4. Install Dependencies
```
pip install -r requirements.txt
```
### 5. Create Necessary Folders
```
mkdir uploads outputs
```
# 6. Run the Application
```
python app.py
```
Once started, open your browser and navigate to the address shown in your terminal
(usually http://127.0.0.1:5000/).
