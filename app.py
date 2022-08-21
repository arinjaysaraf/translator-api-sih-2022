from googletrans import Translator
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"] 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)

class translationClass(BaseModel): 
    sentence:str 
    toLang:str
    fromLang:str 

toLangs = ['en', 'gu', 'hi', 'kn', 'kok', 'mr', 'pa', 'sa', 'ta', 'te']
translatedLangs = {}


@app.post("/")
async def getTrans(translation:translationClass):
    for i in toLangs:
        translator = Translator()
        translated = (translator.translate(translation.sentence, dest= i,src = translation.fromLang))
        translatedLangs[i] = translated.text
    return translatedLangs

#   \n en English(India)
#   \n gu-IN Gujarati(India)
#   \n hi-IN Hindi(India) 
#   \n kn-IN Kannada(India) 
#   \n kok-IN Konkani(India) 
#   \n mr-IN Marathi(India) 
#   \n pa-IN Punjabi(India) 
#   \n sa-IN Sanskrit(India) 
#   \n ta-IN Tamil(India) 
#   \n te-IN Telugu(India)
