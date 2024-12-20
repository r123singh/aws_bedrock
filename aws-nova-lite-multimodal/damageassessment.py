from multimodal import send_image_to_model_using_converse

image_path1= 'images/car_image_before.png'
image_path2 = 'images/car_image_after.png'

system_prompt = '''You are a helpful ai assistant for an insurance agent. Insurance agent has received a claim for a vehicle damage. This claim includes two images. One of the image was taken before the incident and another image was taken after the incident. Analyse these images and answer below questions:
1. describe if there is any damage to the vehicle
2. should insurance agent accept or reject the claim'''

image_list = [
    {
        "image_path": image_path1,
        "message_prompt": "This image was taken when claim was issued"
    },
    {
        "image_path": image_path2,
        "message_prompt": "This image was taken when claim was filed"
    }
]

response = send_image_to_model_using_converse(system_prompt, image_list)

