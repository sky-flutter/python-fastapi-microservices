from pydantic import BaseModel, validator
from datetime import date, datetime
from uuid import uuid4
from typing import Optional

class DobUpdateModel(BaseModel):
    email:str
    dob:str
    
    @validator('email')
    def email_validation(cls,v):
        if v is not None:
            return v
        else:
            raise ValueError("Email is not valid")
    

class LoginUser(BaseModel):
    email: str
    password: str

    @validator('email')
    def email_validation(cls,v):
        if v is not None:
            return v
        else:
            raise ValueError("Email is not valid")
    
    @validator('password')
    def password_validation(cls,v):
        if v is not None and len(v)>6:
            return v
        else:
            raise ValueError("Password must be more than 6 character")

class Users(BaseModel):
    id: str = str(uuid4())
    email: str
    firstName: str
    lastName: str
    mobileNumber: str
    password: str
    profilePic: Optional[str] = None
    dob: date = None
    isActive: bool = True
    isDelete: bool = False
    createdAt: str = datetime.utcnow().isoformat()
    updatedAt: str = datetime.utcnow().isoformat()


    @validator('email')
    def email_validation(cls,v):
        if v is not None:
            return v
        else:
            raise ValueError("Email is not valid")
    
    @validator('password')
    def password_validation(cls,v):
        if v is not None and len(v)>6:
            return v
        else:
            raise ValueError("Password must be more than 6 character")
    
    @validator('firstName')
    def firstName_validation(cls,v):
        if v is not None and len(v)>0:
            return v
        else:
            raise ValueError("Firstname must not be empty")

    @validator('lastName')
    def lastname_validation(cls,v):
        if v is not None and len(v)>0:
            return v
        else:
            raise ValueError("Lastname must not be empty")

    @validator('mobileNumber')
    def mobileNumber_validation(cls,v):
        if v is not None and len(v) >= 10:
            return v
        else:
            raise ValueError("Mobilenumber must be more than 10")

