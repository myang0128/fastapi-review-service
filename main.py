import json

import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from api.review import router
from config import appConfig

app = FastAPI()
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
app.include_router(router)


@app.exception_handler(RequestValidationError)
@app.exception_handler(ValidationError)
def validation_exception_handler(request, exc):
    exc_json = json.loads(exc.json())

    return JSONResponse(exc_json, status_code=422)


@app.exception_handler(ValueError)
def validation_exception_handler(request, exc):
    return JSONResponse({'msg': str(exc)}, status_code=422)


if __name__ == '__main__':
    uvicorn.run(app, debug=True, port=int(appConfig.PORT), host='0.0.0.0')
