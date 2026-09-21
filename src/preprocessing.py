import re
import pandas as pd

TEXT_FIELDS = ["title", "name", "description", "category", "main_category", "sub_category", "brand", "tags", "tag"]

def clean_text(value):
    if pd.isna(value):
        return ""
    value = str(value).strip()
    value = re.sub(r"&amp;", "&", value)
    value = re.sub(r"[^a-zA-Z0-9\s\-,.]", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()

def get_field(product, fields):
    for field in fields:
        if field in product and pd.notna(product[field]):
            value = clean_text(product[field])
            if value:
                return value
    return ""

def build_product_text(product):
    title = get_field(product, ["title", "name"])
    description = get_field(product, ["description"])
    category = get_field(product, ["category", "main_category"])
    sub_category = get_field(product, ["sub_category"])
    brand = get_field(product, ["brand"])
    tags = get_field(product, ["tags", "tag"])

    parts = []

    if title:
        parts.append(f"Product: {title}")

    if description:
        parts.append(f"Description: {description}")

    if category:
        parts.append(f"Category: {category}")

    if sub_category:
        parts.append(f"Subcategory: {sub_category}")

    if brand:
        parts.append(f"Brand: {brand}")

    if tags:
        parts.append(f"Tags: {tags}")

    if not parts:
        return "product"

    return " | ".join(parts)

def prepare_query(query):
    if isinstance(query, dict):
        return build_product_text(query)

    return clean_text(query)