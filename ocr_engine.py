import re


def extract_product_details(ocr_output):
    lines = ocr_output.split("\n")

    quantity_pattern = r"(\d+)"  # Example: Extracts any sequence of digits as quantity
    price_pattern = r"(\d+\.\d+)"  # Example: Extracts decimal numbers as price

    products = []

    for line in lines:
        # Quantity extraction
        quantity_match = re.search(quantity_pattern, line)
        quantity = quantity_match.group(1) if quantity_match else None

        # Price extraction
        price_match = re.search(price_pattern, line)
        price = price_match.group(1) if price_match else None

        # Name extraction
        name = line.strip()  # Example: Assumes the entire line as the product name

        # Store the extracted details as a dictionary
        product_details = {"quantity": quantity, "name": name, "price": price}

        products.append(product_details)

    return products
