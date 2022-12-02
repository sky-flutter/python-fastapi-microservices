from fastapi import APIRouter, UploadFile, File, Form
from .model import Users,LoginUser,DobUpdateModel
from .exception import UserExistsException,UserNotFoundException,UnknownError
from .db import DBHelper
from .s3_handler import S3Helper


users = APIRouter()
dbHelper = DBHelper()
s3Helper = S3Helper()

@users.post('/login')
async def login(payload:LoginUser):
    try:
        item = dbHelper.get_item(payload)
        item.pop("password")
        return {
            "code":200,
            "data": item
        }
    except UserNotFoundException:
        return {
            "code":404,
            "msg":"User not found"
        }



@users.patch('/update/dob')
async def update_dob(dobUpdate:DobUpdateModel):
    try:
        response = dbHelper.update_item(dobUpdate)
        return {
            "code":200,
            "data":response['Attributes']
        }    
    except UnknownError as e:
        return {
            "code": 500,
            "msg": e.message
        }
    except UserNotFoundException:
        return {
            "code": 404,
            "msg": "User not found"
        }

@users.post("/update/profile")
async def create_upload_file(email:str= Form(),file: UploadFile=File()):
    try:
        profilePicName = s3Helper.upload_file(file)
        response = dbHelper.update_profile_pic(email,profilePicName)
        return {
            "statusCode": 200,
            'data':response['Attributes'],
            "message": "Profile updated successfully"
        }
    except UnknownError as e:
        return {
            "code": 500,
            "msg": e.message
        }
    except UserNotFoundException:
        return {
            "code": 404,
            "msg": "User not found"
        }


@users.post('/signup',status_code=201)
async def signup(payload: Users):
    try:
        dbHelper.put_item(payload)
        return {
            "code": 201,
            "msg": "User created successfully"
        }
    except UserExistsException as e:
        return {
            "code": 403,
            "msg": "User already exists"
        }

