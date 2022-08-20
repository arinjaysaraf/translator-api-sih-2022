from googletrans import Translator
from fastapi import FastAPI
from pydantic import BaseModel


class transalationClass(BaseModel): 
    sentence:str 
    toLang:str
    fromLang:str 

app = FastAPI()

@app.post("/")
async def getTrans(translation:transalationClass):
    translator = Translator()
    sentence = """The Prime Minister, Shri Narendra Modi today addressed the Har Ghar Jal Utsav under Jal Jeevan Mission via a video message. The event took place at Panaji Goa. Chief Minister of Goa Shri Pramod Sawant, Union Minister Shri Gajendra Singh Shekhawat were among those present on the occasion. The Prime Minister greeted Shri Krishna devotees on the auspicious occasion of Janmashtami.

    At the outset, the Prime Minister shared every Indian’s pride in three important milestones related to the huge goals that India is working on in Amrit Kaal, that were accomplished today. He said “Firstly, today 10 crore rural households of the country have been connected to piped clean water facility. This is a big success of the government's campaign to deliver water to every household. This is a great example of ‘Sabka Prayas’”. Secondly, he congratulated Goa for becoming the first Har Ghar Jal certified state where every household is connected to piped water. He also acknowledged Dadra Nagar Haveli and Daman and Diu as first Union territories to achieve the feat. The Prime Minister lauded the people, government and local self-government institutions for their efforts. He informed that many states are going to join the list very soon.

    The third achievement, the Prime Minister informed, is that one lakh villages in different states of the country have turned ODF plus. After the country was declared Open Defecation Free (ODF) a few years ago, the next resolution was to achieve ODF plus status for villages i.e. they should have community toilets, plastic waste management, grey water management and Gobardhan projects"""
    translated = (translator.translate(translation.sentence, dest= translation.toLang,src = translation.fromLang))
    return (translated.text)