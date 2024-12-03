import openai
import time

openai.api_key = ''

def chat_with_gpt(user_input):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[{
                "role": "user",
                "content": user_input
            }]
        )
        return response.choices[0].message.content.strip()
    except openai.error.RateLimitError as e:
        print(f"Rate limit error: {e}")
        time.sleep(60)  # Wait for 60 seconds before retrying
        return chat_with_gpt(user_input)  # Retry after waiting

if __name__ == '__main__':
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            break
        response = chat_with_gpt(user_input)
        print(f"Chatbot: {response}")
