from fastapi import FastAPI
from dotenv import load_dotenv
import os
from openai import OpenAI


# Env File
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)



app = FastAPI()

@app.get("/")
def main():
  return {"Message": "Hello World"}


@app.post("/test")
async def scan_entities(text):
  
  response = client.responses.create(
    model="gpt-4o-mini",
    input=text
  )

  return {"Entities": response}



