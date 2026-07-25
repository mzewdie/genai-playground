import ollama

from ollama import chat
from ollama import ChatResponse
#from ollama import ChatResponse, chat



#print(ollama)
#print(dir(ollama))

response: ChatResponse = chat(model='gemma3', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)