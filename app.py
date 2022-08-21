from googletrans import Translator
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"] 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)
class transalationClass(BaseModel): 
    sentence:str 
    toLang:str
    fromLang:str 


@app.post("/")
async def getTrans(translation:transalationClass):
    translator = Translator()
    translated = (translator.translate(translation.sentence, dest= translation.toLang,src = translation.fromLang))
    return (translated.text)