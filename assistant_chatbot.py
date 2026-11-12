# Lets the program read environment variables - so that we can store the API key in a secure way
import os
# Imports the Google GenAI client library so that we can use the Gemini API
from google import genai
# Imports the types module from the Google GenAI library so that we can use the GenerateContentConfig class
from google.genai import types
# Imports the sys module so that we can exit the program if the API key is not set
import sys

# Gets the API key from the environment variable GEMINI_API_KEY
api_key = os.environ.get("GEMINI_API_KEY")
# Exits the program if the API key is not set
if not api_key:
    raise SystemExit("Set the GEMINI_API_KEY environment variable first.")

# Creates a client object that we can use to interact with the Gemini API
client = genai.Client(api_key=api_key)

# Reads the system instruction from a text file and stores it in a variable
try:
    with open('chat_system_instruction.txt', 'r') as f:
        system_instruction_text = f.read()
# Exits the program if the system instruction file is not found
except:
    print("Missing system instruction, quiting program")
    sys.exit()

# Starts an infinite loop that will keep asking the user for input and generating responses from the Gemini API
while True:
    # Prompts the user for input and stores it in a variable
    question = input("> ")
    # Exits the loop if the user types "exit"
    if question.lower() == "exit":
        break
    # Calls the generate_content method of the client object to generate a response from the Gemini API
    response = client.models.generate_content(
        # Specifies the model to use for generating content
        model="gemini-3.1-flash-lite",
        # Specifies the user's input as the content to generate a response for
        contents=question,
        # Specifies the system instruction to use for generating the response
        config=types.GenerateContentConfig(
            # Specifies the system instruction to use for generating the response
            system_instruction=system_instruction_text
        )
    )
    # Prints the generated response from the Gemini API to the console
    print(response.text)