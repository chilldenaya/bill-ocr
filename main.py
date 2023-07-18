import io

import pytesseract
from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from PIL import Image

from ocr_engine import extract_product_details

app = FastAPI()


@app.post("/extract_product_details")
async def extract_product_details_api(file: UploadFile = UploadFile(...)):
    # Check if the uploaded file is an image
    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400, detail="Invalid file format. Only images are supported."
        )

    # Read the uploaded image file
    image = Image.open(io.BytesIO(await file.read()))

    # Perform OCR on the image
    ocr_output = pytesseract.image_to_string(image)

    # Extract product details from OCR output
    product_details = extract_product_details(ocr_output)

    return product_details


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title=app.title + " - Swagger UI",
        oauth2_redirect_url="/docs/oauth2-redirect",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get("/openapi.json", include_in_schema=False)
async def get_openapi_json():
    return _custom_openapi()


def _custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Your API Title",
        version="1.0.0",
        description="Your API Description",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema
