from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
from openai import OpenAI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


# Env File
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

class InputText(BaseModel):
  text: str


app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/")
def main():
  return {"Message": "Hello World"}


@app.post("/scan_entities")
async def scan_entities(body: InputText):
  if not body.text.strip():
    raise HTTPException(status_code=400, detail="Tekst mag niet leeg zijn")
  
  response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "Je bent een AI die entiteiten uit teksten herkent. Je moet de entiteiten in de tekst herkennen en deze retourneren in een JSON-formaat."},
        {"role": "user", "content": body.text}
    ]
  )


  return {"Entities": response}



