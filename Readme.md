# FastAPI OCR Bill Splitter

This project is a FastAPI application that provides an endpoint for splitting bills using OCR (Optical Character Recognition). It extracts quantity, name, and price information from an uploaded bill image and returns the details as a response.

**_Notes: the `quantity-name-price` extractor is still in progress_**

## Prerequisites

- Python 3.7 or higher
- Tesseract OCR
- Additional dependencies (specified in requirements.txt)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate # Linux/Mac
   env\Scripts\activate # Windows
   ```

   or use conda

3. Install Tesseract OCR:

   ```
   sudo apt-get install tesseract-ocr
   ```

4. Install the required dependencies:

   ```bash
    pip install -r requirements.txt
   ```

## Usage

1. Run the FastAPI server:

```
uvicorn main:app --reload
```

2. Open your browser and navigate to http://localhost:8000/docs to access the Swagger UI.

3. Upload an image of the bill using the provided endpoint to perform OCR and extract the quantity, name, and price details.
