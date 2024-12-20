import streamlit as st
import os
import google.generativeai as genai 
import re

# Get the API key from the environment variable
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("API key not found. Make sure GOOGLE_API_KEY is set as an environment variable.")

genai.configure(api_key=api_key)

# Model generation configuration
generation_config = {
  "temperature": 0.1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 100,
  "response_mime_type": "text/plain",
}

# Initialize the model
model = genai.GenerativeModel(
  model_name="tunedModels/finetunedata-kqn02hc20o4y",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[]
)

def sent_tokenize(text):
    # Split the text by common sentence-ending punctuation (., !, ?)
    sentences = re.split(r'(?<=[.!?]) +', text)
    return sentences

# Streamlit interface
st.title('E-mail Tone Analyzer')

# Create a multi-line text input box (textarea) for the user to enter email body
user_input = st.text_area("Enter the body of your e-mail:")
analyze_button = st.button("Analyze")

# Check if the user input is empty and handle the situation
if user_input.strip() == "":
    st.warning("Please enter some text to analyze.")
else:
    sentences = sent_tokenize(user_input)
    try:
        # Sending the user input to the model for tone analysis
        for sent in sentences:
          st.write(sent)
          response = chat_session.send_message(sent)
          st.write("Tone:", response.text)  # Display the tone of the email as generated by the model
          st.write("----------")
        overall_res = chat_session.send_message(user_input)
        st.markdown(f"**Overall Tone: {overall_res.text}**")
        

    except ValueError as e:
        st.error(f"Error: {str(e)}")

