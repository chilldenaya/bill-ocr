import re
import pytesseract
import cv2
import numpy as np


def preprocess_image(image):
    image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)

    return image


def get_bill_string(image):
    custom_config = r"-c tessedit_char_blacklist=:*-;!@#$%^&*(){} --oem 3 --psm 6"
    return pytesseract.image_to_string(image, config=custom_config)


def extract_product_details(ocr_output):
    lines = ocr_output.split("\n")
    quantity_pattern = r"(\d+)"
    price_pattern = r"(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d+)?)|\d+(?:[.,]\d+)?"

    products = []
    print(lines)
    for line in lines:
        quantity_match = re.search(quantity_pattern, line)
        quantity = quantity_match.group(1) if quantity_match else None

        price_match = re.search(price_pattern, line)
        price = price_match.group(1) if price_match else None

        name = line.strip()

        product_details = {
            "quantity": int(quantity) if quantity is not None else quantity,
            "name": name,
            "price": price,
        }

        should_add_to_products = True
        for k, v in product_details.items():
            if v is None:
                should_add_to_products = False

            if k == "quantity" and type(v) != int:
                should_add_to_products = False

        if should_add_to_products:
            products.append(product_details)

    return products
