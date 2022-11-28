from fastapi import FastAPI
from fastapi.responses import Response
from pydantic import BaseModel
import re

class Item(BaseModel):
    phone: str

app = FastAPI()


@app.post("/unify_phone_from_json")
def index_page(item: Item):
    numbers_only = re.sub(r'\D', '', item.phone)
    if not len(numbers_only) in [11,10]:
            return numbers_only
    if len(numbers_only)==11:
        numbers_only='8'+ numbers_only[1:]
    if len(numbers_only)==10:
        numbers_only='8'+ numbers_only
    numbers_only = re.sub(r'(\d{1})(\d{3})(\d{3})(\d{2})(\d{2})',
                                    r'\1 (\2) \3-\4-\5', numbers_only)    
    return numbers_only
