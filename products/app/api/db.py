import boto3
import sys
from .model import ProductRequest
from botocore.exceptions import ClientError
from config import Config

sys.path.append("./")

class DBHelper:
    
    def __init__(self) -> None:
        self.tableName = "Products"
        self.db = boto3.resource("dynamodb",aws_access_key_id=Config.AWS_ACCESS_KEY,aws_secret_access_key=Config.AWS_SECRET_KEY,region_name=Config.AWS_REGION)
    
    def get_table(self,tableName):
        return self.db.Table(tableName)

    def put_item(self,product:ProductRequest):
        try:
            self.get_table(self.tableName).put_item(Item=product.dict())
        except ClientError as e:
            raise 

    def get_detail(self,sku:str):
        return self.get_table(self.tableName).query(KeyConditionExpression="sku=:sku",ExpressionAttributeValues={':sku':sku})

    def paginate(self,pageSize:int,lastEvaluateKey:dict=None):
        return self.get_table(self.tableName).scan()