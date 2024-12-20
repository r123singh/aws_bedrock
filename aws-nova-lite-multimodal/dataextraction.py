from multimodal import send_image_to_model_using_converse

system_prompt = """
You are a prompt analyst your is to analyze images provided and output the information in the exact JSON structure specified below. Ensure that you populate each field accurately based on the visible details in the page. If any information is not available or cannot be determined, use 'Unknown' for string fields and empty array [] for lists

Use the format shown exactly, ensuring all fields and values align with JSON schema requirements.

Use this JSON schema:
{
    "title" : "string",
    "description": "string",
    "category": {
        "type": "string",
        "enum": ["Electronics", "Furniture", "Luggage", "Clothing", "Appliances", "Toys", "Books", "Tools", "Other"]
    },
    "metadata": {
        "color":{
            "type": "array",
            "items": {"type": "string"}
        },
        "shape":{
            "type": "string",
            "enum": ["Round", "Square", "Rectangular", "Irregular", "Other"]
        },
        "condition": {
            "type": "string",
            "enum": ["New", "Like New", "Good", "Fair", "Poor", "Unknownn"]
        },
        "material": {
            "type": "array",
            "items": {"type": "string"}
        },
        "brand": {"type": "string"}
    },
    "image_quality": {
        "type": "string",
        "enum": ["High", "Medium", "Low"]
    },
    "background": "string",
    "additional_features": {
        "type": "array",
        "items": {"type": "string"}
    }
}
"""
image_path = "images/dresser.png"
image_list = [
    {
        "image_path": image_path,
        "message_prompt": "product picture"
    }]
response = send_image_to_model_using_converse(system_prompt, image_list)