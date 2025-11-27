from google import genai
import os
# from dotenv import load_dotenv


# load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))



chat = client.chats.create(model ="gemini-2.0-flash")

while True:
    
    user_input = input("> : ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat.")
        break

    response = chat.send_message(user_input)
    print("Bot:", response.text)



    