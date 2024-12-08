# Importing the os library to interact with the operating system.
# This will be used to retrieve environment variables.
import os

# Importing the Google Generative AI library to interact with Generative AI models.
import google.generativeai as genai

# Retrieving the API key for Google Generative AI from environment variables.
# The API key is required to authenticate requests to the Generative AI service.
api_key = os.getenv("GENAI_API_KEY")

# Configuring the Generative AI library with the retrieved API key.
# This step ensures that all subsequent API calls are authenticated.
genai.configure(api_key=api_key)

# Defining the configuration for the generative model.
# These parameters control the behavior and output of the model.
generation_config = {
    "temperature": 0.1,  # Controls the randomness of the model's responses (lower is more deterministic).
    "top_p": 0.95,      # Controls nucleus sampling; the model considers tokens with a cumulative probability of top_p.
    "top_k": 40,        # Controls the number of top tokens to consider for sampling.
    "max_output_tokens": 100,  # Limits the maximum number of tokens in the output.
    "response_mime_type": "text/plain",  # Specifies the format of the response (plain text in this case).
}

# Initializing a generative model instance with a specific fine-tuned model.
# Replace "tunedModels/finetunedata-kqn02hc20o4y" with the name of your fine-tuned model.
model = genai.GenerativeModel(
    model_name="tunedModels/finetunedata-kqn02hc20o4y",
    generation_config=generation_config,
)

# Starting a new chat session using the generative model.
# The `history` parameter can include previous messages to provide context for the conversation.
chat_session = model.start_chat(
    history=[]  # No prior conversation history; starting a fresh session.
)

# Sending a user-provided input to the model and receiving the response.
# The input() function allows the user to type a message, which is then sent to the model.
response = chat_session.send_message(input())

# Printing the text content of the model's response to the console.
# This displays the generated reply based on the input and the configured model parameters.
print(response.text)
