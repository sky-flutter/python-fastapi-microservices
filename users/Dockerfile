FROM python:3.10-alpine

WORKDIR /app

COPY  requirements.txt .

RUN pip install -r requirements.txt

ENV AWS_BUCKET_NAME=
ENV AWS_ACCESS_KEY=
ENV AWS_SECRET_KEY=
ENV AWS_REGION=

COPY . .

EXPOSE 3001

CMD [ "python","app/main.py" ]
