from fastapi import FastAPI
import pandas as pd
import chardet
from pymongo import MongoClient
import pydantic
from bson.objectid import ObjectId
import os.path
import json

pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, '../secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

HOSTNAME = get_secret("ATLAS_Hostname")
USERNAME = get_secret("ATLAS_Username")
PASSWORD = get_secret("ATLAS_Password")

client = MongoClient(f'mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}')
print('Connected to MongoDB....')

#test에 projectFiredb로 넣어준다.
mydb = client['test']
mycol = mydb['projectFiredb']

@app.get('/')
def healthCheck():
    return "OK"

@app.get('/getmongo')
async def getMongo():
    return list(mycol.find())

#yearmonth Select
@app.get('/getdata')
async def getdata(yearmonth=None):
    if yearmonth is None:
        return "날짜를 입력하세요."
    result = mycol.find_one({"yearmonth":yearmonth})
    if result:
        return result
    else:
        return "검색 결과가 없습니다."

#Json Data insert
@app.get('/add_data')
async def add_data():
    with open("산불월별발생횟수.json", "r") as file:
        data = json.load(file)

    for item in data:
        mycol.insert_one(item)

    return "데이터가 추가되었습니다."