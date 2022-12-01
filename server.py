from fastapi import FastAPI, Form, Cookie
from fastapi.responses import  Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import sys
import re

from loguru import logger

logger.remove()
logger.add(sys.stderr, level="DEBUG")
logger.add("debug.log", rotation= '1 day')

class Item(BaseModel):
    phone: str

app = FastAPI()


def beautify(phone:str)->str:
    numbers_only = re.sub(r'\D', '', phone)
    if not len(numbers_only) in [11,10]:
            return numbers_only
    if len(numbers_only)==11:
        numbers_only='8'+ numbers_only[1:]
    if len(numbers_only)==10:
        numbers_only='8'+ numbers_only
    numbers_only = re.sub(r'(\d{1})(\d{3})(\d{3})(\d{2})(\d{2})',
                                    r'\1 (\2) \3-\4-\5', numbers_only)    
    return Response(content= numbers_only, media_type = "text/html")
 


@app.post("/unify_phone_from_json")
def index_page(item: Item):
    logger.info("Started working on new request")
    print('srabotalo')
    numbers_only = re.sub(r'\D', '', item.phone)
    if not len(numbers_only) in [11,10]:
            return numbers_only
    if len(numbers_only)==11:
        numbers_only='8'+ numbers_only[1:]
    if len(numbers_only)==10:
        numbers_only='8'+ numbers_only
    numbers_only = re.sub(r'(\d{1})(\d{3})(\d{3})(\d{2})(\d{2})',
                                    r'\1 (\2) \3-\4-\5', numbers_only)    
    numbers_only = numbers_only
    json_compatible_phone = jsonable_encoder(numbers_only)
    return Response(content= numbers_only, media_type = "text/html")



@app.post("/unify_phone_from_form")
def unify_phone_from_form(phone: str = Form()):
    numbers_only = re.sub(r'\D', '', phone)
    if not len(numbers_only) in [11,10]:
            return numbers_only
    if len(numbers_only)==11:
        numbers_only='8'+ numbers_only[1:]
    if len(numbers_only)==10:
        numbers_only='8'+ numbers_only
    numbers_only = re.sub(r'(\d{1})(\d{3})(\d{3})(\d{2})(\d{2})',
                                    r'\1 (\2) \3-\4-\5', numbers_only)    
    return Response(content= numbers_only, media_type = "text/html")


@app.get("/unify_phone_from_query")
def unify_phone_from_query(phone: str = ''):
    return beautify(phone)

@app.get("/unify_phone_from_cookies")
def unify_phone_from_cookies(phone: str | None = Cookie(default=None)):
    return beautify(phone)
