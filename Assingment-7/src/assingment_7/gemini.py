from litellm import completion
import os
from dotenv import load_dotenv

load_dotenv()
def llm():
    messages = [{"role": "user", "content": "What is the current economic trends in the world?"}]
    llm = completion(model ="gemini/gemini-2.0-flash-exp" ,api_key=os.getenv("GOOGLE_API_KEY"),messages=messages )
    print(llm['choices'][0]['message']['content'])

def llm2():
    messages = [{"role": "user", "content": "What is the current economic trends in the world?"}]
    llm = completion(model ="groq/llama-3.3-70b-versatile" ,api_key=os.getenv("Groq_API_KEY") ,messages=messages )
    print(llm['choices'][0]['message']['content'])