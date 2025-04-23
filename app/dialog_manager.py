
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_response(user_input, context=""):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful health assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return response['choices'][0]['message']['content']
