import openai
import os

# Set up your API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define a function that takes user input and sends it to ChatGPT

last_response = "";

def chat_gpt(user_input, last_answer):
    
    messages = [
                  { "role": "system", "content": "You are a helpful assistant." },
                  { "role": "assistant", "content": last_answer},
                  { "role": "user", "content": user_input}
                ]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        max_tokens=256
    )
    
    return response.choices[0].message.content   
    


# Loop to ask for user input and receive ChatGPT's response
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("ChatGPT: Goodbye!")
        break
    
    response = chat_gpt(user_input, last_response)
    print("ChatGPT:", response)
    
    last_response = response;
    