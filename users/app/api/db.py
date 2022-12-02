import boto3
import sys
from .model import LoginUser,Users,DobUpdateModel
from botocore.exceptions import ClientError
from .exception import UserNotFoundException, UnknownError
from config import Config

sys.path.append("./")
class DBHelper:
    
    def __init__(self) -> None:
        self.tableName = "Users"
        self.db = boto3.resource("dynamodb",aws_access_key_id=Config.AWS_ACCESS_KEY,aws_secret_access_key=Config.AWS_SECRET_KEY,region_name=Config.AWS_REGION)
    
    def get_table(self,tableName):
        return self.db.Table(tableName)

    def put_item(self,users:Users):
        try:
            self.get_table(self.tableName).put_item(Item=users.dict())
        except ClientError as e:
            raise 
    
    def get_item(self,login:LoginUser):
        user = self.get_table(self.tableName).get_item(Key={'email':login.email})
        if 'Item' in user:
            return user['Item']
        else:
            raise UserNotFoundException("User not found")
    def update_profile_pic(self,email,profilePicUrl):
        try:
            return self.get_table(self.tableName).update_item(
                Key={'email':email},
                ConditionExpression="attribute_exists(#e)",
                UpdateExpression="set #photo = :photo",
                ExpressionAttributeNames={'#photo':'ProfilePic','#e':'email'},
                ExpressionAttributeValues={':photo': profilePicUrl},
                ReturnValues="UPDATED_NEW"
            )
        except ClientError as e:
            if e.response['Error']['Code'] == "ConditionalCheckFailedException":
                raise UserNotFoundException()
            raise UnknownError(e.response['Error']['Message'])

    def update_item(self,dobUpdate:DobUpdateModel):
        try:
            return self.get_table(self.tableName).update_item(
                Key={'email':dobUpdate.email},
                ConditionExpression="attribute_exists(#e)",
                UpdateExpression="set #dob = :dob",
                ExpressionAttributeNames={'#dob':'dob','#e':'email'},
                ExpressionAttributeValues={':dob': dobUpdate.dob},
                ReturnValues="UPDATED_NEW"
            )
        except ClientError as e:
            if e.response['Error']['Code'] == "ConditionalCheckFailedException":
                raise UserNotFoundException()
            raise UnknownError(e.response['Error']['Message'])
        