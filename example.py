import json
import os
import openai

user_input = input("Simply describe what you want to see in HTML:\n")

print("\nLet me see what I can do...\n")

with open('keys.json') as f:
  keys = json.load(f)

openai.api_key = keys['openapi']

full_request = "Q: HTML for " + user_input +  "\nA:"

response = openai.Completion.create(engine="davinci", prompt=full_request, 
temperature=0,
  max_tokens=300,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop="\nQ:")

print(response.choices[0].text)