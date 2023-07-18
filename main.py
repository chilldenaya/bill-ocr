import io

from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from PIL import Image

import ocr_engine

app = FastAPI()


@app.post("/extract_product_details")
async def extract_product_details_api(file: UploadFile = UploadFile(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400, detail="Invalid file format. Only images are supported."
        )

    original_image = Image.open(io.BytesIO(await file.read()))
    processed_image = ocr_engine.preprocess_image(original_image)

    ocr_output = ocr_engine.get_bill_string(processed_image)
    product_details = ocr_engine.extract_product_details(ocr_output)

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
