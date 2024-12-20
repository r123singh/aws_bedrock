import multimodal
from multimodal import send_image_to_model_using_converse

image_path = 'images/animal.jpg'
system_prompt = 'You are an expert wildlife explorer. When the user provides you with an image, provide a hilarious response'
image_list = [{
    "image_path": image_path,
    "message_prompt": system_prompt
}]
response = send_image_to_model_using_converse(system_prompt, image_list)
