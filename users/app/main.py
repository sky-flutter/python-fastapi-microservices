import uvicorn
from fastapi import FastAPI,Request,status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from api.users import users
app = FastAPI()

app.include_router(users,prefix="/user")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_dict={}
    for error in exc.errors():
       error_dict[error['loc'][-1]]=error['msg']
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"error": error_dict,"code":400}),
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3001, reload=True)
