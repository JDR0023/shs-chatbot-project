# Chat bot skeleton framework
# To run, type in terminal: python main.py
# Don't forget to pip install google-generativeai first! (pip install google-generativeai)

import google.generativeai as genai
import os

# 1. API Key
genai.configure(api_key="YOUR_API_KEY_HERE")

# 2. Define the "System Instruction"
# This is where you put all the facts about your SHS.
school_info = """
You are a helpful assistant for [Name of your School] Senior High School. 
Answer questions based on these facts:
- The Principal is Mr. Juan Dela Cruz.
- SHS strands offered: STEM, ABM, HUMSS, and ICT.
- Class hours: 7:00 AM to 4:00 PM.
- The school uniform for STEM is a white polo with a green tie.
- The library is located on the 3rd floor of the Main Building.
- For enrollment inquiries, contact the registrar at registrar@school.edu.
"""

# 3. Initialize the Model
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash", 
    system_instruction=school_info
)

# 4. Start a Chat Session
chat = model.start_chat(history=[])

print("Welcome to the SHS Help Desk! (Type 'quit' to stop)")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        break
    
    response = chat.send_message(user_input)
    print(f"Bot: {response.text}\n")