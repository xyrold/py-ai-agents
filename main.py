import requests
from langchain_ollama import OllamaLLM

ollama_model = OllamaLLM(model="llama3.2")


# Function to get user information from the FastAPI API
def get_user_info(user_id: int):
    url = f"http://127.0.0.1:8000/api/test/{user_id}"
    headers = {
        'x-api-key': "cErmMfZieNADjjQ7T3iu9VXxgJWhAkJq"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        user_data = response.json()
        return user_data
    else:
        return None

# AI Assistant function that integrates with Langchain Ollama and the API
def ai_assistant(prompt: str):

    template = (
                "You are acting as a support agent, and your tasked is to respond to the user's query: {query}."
                "Identify if the user's query is general information or information that you need to use api call."
                "Respond 'need api call' if you don't know the answer and give the context, and if you know the answer respond with information"
        )
    prompt_with_user_info = template.format(query=prompt)
    # if "check my account" in prompt.lower():
    #      else:
    #     prompt_with_user_info = prompt
    user_info = None #get_user_info(1)
    # if user_info:
    #     # template = (
    #     #         "You are tasked with providing information from the following text content: {user_data}. "
    #     #         "**Extract Information:** extract the information that directly matches the provided description: {parse_description}. and respond with sentence based on the question."
    #     # )
    #     prompt_with_user_info = template.format(user_data=user_info, parse_description=prompt)
    # else:
    #     prompt_with_user_info = prompt
   
    # print(user_info)

    prompts = [prompt_with_user_info]
    # Generate a response using Langchain Ollama
    response = ollama_model.generate(prompts)

    return response.generations[0][0].text

def extract_text_from_generation(generation):
    # Assuming 'generation' is a list of GenerationChunk objects
    if generation and 'text' in generation[0]:
        return generation[0]['text']
    return ''

# Example usage
# if __name__ == "__main__":
#     prompt = "what is my name"
#     # user_id = 1  # Example user ID
#     response = ai_assistant(prompt)
#     print(response)

def main():
    print("\nWelcome to the AI Assistant CLI! Type your prompt or 'exit' to quit.")

    while True:
        prompt = input("\n> ")
        if prompt.lower() == 'exit':
            print("Exiting...")
            break

        response = ai_assistant(prompt)
        print(f"\nResponse: {response}")

if __name__ == "__main__":
    main()

# def main():
#     try:
#         # Initialize the OllamaLLM with default settings
#         llm = OllamaLLM(model="llama3.2")

#         # Test a simple query
#         query = ["What is the capital of France?"]
#         response = llm.generate(query)

#         # Print the response
#         print("Response from Ollama:")
#         print(response)

#     except Exception as e:
#         print("An error occurred:")
#         print(e)

# if __name__ == "__main__":
#     main()
