import boto3
import json
import base64
from PIL import Image

bedrock_client = boto3.client('bedrock-runtime', region_name = 'us-east-1')

MODEL_ID = 'us.amazon.nova-lite-v1:0'

def read_and_encode_image(image_path, message_prompt):
    """
    Reads an image from a local file path and encodes it to a data URL
    Args:
        image_path (_type_): _description_
        message_prompt (_type_): _description_
    """
    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()
        
    base64_encoded = base64.b64encode(image_bytes).decode('utf-8')
    # Determine the image format -jpg,gif,jpeg
    image_format = Image.open(image_path).format.lower()

    message_content = {
        "image": {
            "format": image_format,
            "source": {"bytes": image_bytes}
        }
    }
    
    return message_content

def send_image_to_model_using_converse(system_prompt: str, image_list: list):
    """_summary_
    Sends images and a prompt to the model and returns the response in the plain text
    Args:
        system_prompt (str): _description_
        image_list (list): _description_
    """
    content_list = []
    for img in image_list:
        message_content = read_and_encode_image(img['image_path'], img['message_prompt'])
        content_list.append(message_content)
        content_list.append({'text': img['message_prompt']})
    
    system = [{"text": system_prompt}] 
    # Define a "user" message including both the image and a text prompt
    messages = [
        {
            "role": "user",
            "content": content_list
        }
    ]   
    
    #Configure the inference parameters
    inf_params = {"maxTokens": 500, "temperature": 1.0}
    
    response = bedrock_client.converse(
        modelId = MODEL_ID,
        messages = messages,
        system = system
    )
    
    output_message = response['output']['message']
    print("\n[Response Content Text]")
    for content in output_message['content']:
        print(f"{content['text']}")
    
    token_usage = response['usage']
    print("\t-- Token Usage ---")
    print(f"\tInput tokens: {token_usage['inputTokens']}") 
    print(f"\tOutput tokens: {token_usage['outputTokens']}")
    print(f"\tTotal tokens: {token_usage['totalTokens']}")
    print(f"\tStop reason: {response['stopReason']}")
    
    return output_message

