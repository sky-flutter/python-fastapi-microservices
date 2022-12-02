
# Python FastAPI microservices

This project is demonstrate to those who wants to work with microservices in python. I have created demo APIs for users and products module. I have created API using AWS dynamodb and AWS S3 service.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`AWS_ACCESS_KEY`

`AWS_SECRET_KEY`

`AWS_REGION`

`AWS_BUCKET_NAME`


## Run Locally

Clone the project

```bash
  git clone https://github.com/sky-flutter/python-fastapi-microservices.git
```

Go to the project directory

```bash
  cd python-fastapi-microservices
```

Run docker-compose.yaml

```bash
  docker compose up
```

Hit API URL in postman

```bash
  http://localhost:8085/api/v1/user
  http://localhost:8085/api/v1/product
```

