from fastapi import APIRouter
from .model import ProductRequest
from botocore.exceptions import ClientError
from .db import DBHelper
from typing import List


products = APIRouter()
dbHelper = DBHelper()


@products.get("/list")
def list_product(page:int=1,pageSize:int=4):
    try:
        # if page == 1:
        #     response = dbHelper.paginate(pageSize)    
        # else:
        #     response = dbHelper.paginate(pageSize,lastEvaluatedKey=lastEvaluatedKey)
        response = dbHelper.paginate(pageSize)    
        # lastEvaluatedKey = response['LastEvaluatedKey']
        return {
            "code": 200,
            "data": response['Items'],
        }
    except ClientError as e:
        print(e)

@products.get("/detail")
def detail(sku:str):
    try:
        data = dbHelper.get_detail(sku=sku)
    except ClientError as e:
        return {
            "code": 404,
            "msg": "Product not found"
        }
    else:
        return {
            "code": 200,
            "data": data["Items"][0]
        }

@products.post("/create/new")
def create_product(request:List[ProductRequest]):
    try:
        table = dbHelper.get_table(dbHelper.tableName)
        with table.batch_writer() as batch:
            for item in request:
                batch.put_item(Item=item.dict())

    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            return {
                "code": 500,
                "msg": "Product already in the database"
            }
        else:
            return {
                "code": 500,
                "msg": "Something went wrong."
            }
    else:
        return {
            "code": 200,
            "msg": "Product added successfully"
        }

    
