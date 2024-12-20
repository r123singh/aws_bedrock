from multimodal import send_image_to_model_using_converse

system_prompt = """
Analyze the attached image of the chart or graph. Your tasks are to:

Identify the type of chart or graph (e.g., bar chart, line graph, pie chart etc.).
Extract the key data points, including labels, values, and any relevant scales or units.
Identify and describe the main trends, patterns, or significant observations presented in the chart.
Generate a clear and concise paragraph summarizing the extracted data and insights. The summary should highlight the most important information and provide an overview that would help someone understand the chart without seeing it.
Ensure that your summary is well-structured, accurately reflects the data, and is written in a professional tone
"""

image_path = "images/amazon_chart.png"
image_list = [
    {
        "image_path": image_path,
        "message_prompt": "chart picture"
    }
]

response = send_image_to_model_using_converse(system_prompt, image_list)