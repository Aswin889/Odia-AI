from fastapi import FastAPI
from pydantic import BaseModel
from googletrans import Translator

app = FastAPI()

translator = Translator()

class RequestData(BaseModel):
    text: str
    language: str

lang_map = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "Mandarin Chinese": "zh-cn"
}

@app.post("/translate")
def translate(data: RequestData):

    result = translator.translate(
        data.text,
        dest=lang_map[data.language]
    )

    return {
        "translation": result.text
    }
