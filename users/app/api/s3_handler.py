import boto3
import sys
from werkzeug.utils import secure_filename
from config import Config

sys.path.append("./")
s3 = boto3.client("s3",aws_access_key_id=Config.AWS_ACCESS_KEY,aws_secret_access_key=Config.AWS_SECRET_KEY,region_name=Config.AWS_REGION)


bucket_location = s3.get_bucket_location(Bucket=Config.AWS_BUCKET_NAME)


class S3Helper:
    def upload_file(self,profile_pic,acl="public-read"):
        
        filename = secure_filename(profile_pic.filename)
        try:
            s3.upload_fileobj(
                profile_pic,
                Config.AWS_BUCKET_NAME,
                filename,
                ExtraArgs = {
                    "ACL":acl,
                    "ContentType": profile_pic.content_type
                }
            )
        except Exception as e:
            print("Something Happened: ",e)

        return "https://{0}.s3.{1}.amazonaws.com/{2}".format(Config.AWS_BUCKET_NAME,bucket_location['LocationConstraint'],filename)