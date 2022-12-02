import os

class Config:
    AWS_BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')
    AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
    AWS_REGION = os.environ.get('AWS_REGION')