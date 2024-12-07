import os
import google.generativeai as genai

api_key = os.getenv("GENAI_API_KEY")
genai.configure(api_key=api_key)

# Create the model
generation_config = {
  "temperature": 0.1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 100,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="tunedModels/finetunedata-kqn02hc20o4y",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message(input())

print(response.text)

