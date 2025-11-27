from google import genai
import os
from dotenv import load_dotenv


load_dotenv()


# The client gets the API key from the environment variable `GEMINI_API_KEY`.
# from google import genai


api_key_google = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key_google)


user_input = input("Enter your question: ")


response = client.models.generate_content(
    model = "gemini-2.0-flash",
    contents=user_input
)


print(response.text)




# ---------------------------------------------------------------------------- #





from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client(api_key=api_key_google)



user_input = input("Enter your text to convert to speech: ")

response = client.models.generate_content(
   model="gemini-2.5-flash-preview-tts",
   contents=f"Say cheerfully: {user_input}",
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
               voice_name='Kore',
            )
         )
      ),
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='out.mp3'
wave_file(file_name, data) # Saves the file to current directory