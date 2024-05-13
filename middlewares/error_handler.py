
from starlette.middleware.base import BaseHTTPMiddleware

from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from fastapi import FastAPI


class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app:FastAPI ) -> None:
        super().__init__(app)

    
    def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            return call_next(request)
        except Exception as ex:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"error":str(ex)}
                )
