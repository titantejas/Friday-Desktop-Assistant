import requests

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
TOKEN = "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"  

headers = {"Authorization": f"Bearer {TOKEN}"}

def image_bytes(query: str, width: int = 1080, height: int = 720) -> bytes:
    """
    Function to generate image bytes from a query.
    :param query: Description of the image to generate
    :return: Image bytes
    """
    payload ={
            "inputs": query,
            "parameters": {
            "width": width,
            "height": height
        }
      }         
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.content  
    else:
        raise Exception(f"API Error: {response.status_code}, {response.text}")