#from openai import OpenAI
import openai
import os
from dotenv import load_dotenv
load_dotenv()

# Set your API key
api_key = os.getenv('OPENAI_API_KEY')

if api_key is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

openai.api_key = api_key

# Generate an image
response = openai.images.generate(
     model="dall-e-3",
    prompt="An astronaut riding a futuristic sportbike on a racetrack under a dramatic sky",
    size="512x512",
    quality="standard",
    n=1
)

# URL of the generated image
image_url = response.data[0].url
print("Generated Image URL:", image_url)
