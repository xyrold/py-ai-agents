from flask import Flask, request, jsonify
from flask_cors import CORS 
import openai
import os
from dotenv import load_dotenv
load_dotenv()

# Set your API key
api_key = os.getenv('OPENAI_API_KEY')

if api_key is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set")


app = Flask(__name__)
CORS(app)
# Set your OpenAI API key
openai.api_key = api_key

@app.route('/api/generate-image', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get('prompt', '') if data else ''

    try:
        # Call OpenAI API or another model to generate the image
        response = openai.images.generate(
            model="dall-e-3",
            prompt=prompt, #"An astronaut riding a futuristic sportbike on a racetrack under a dramatic sky",
            size="1024x1024",
            quality="standard",
            n=1
        )
        image_url = response.data[0].url
        return jsonify({"image_url": image_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
