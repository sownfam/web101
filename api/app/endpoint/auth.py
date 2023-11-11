from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.app.dto.core.auth import SignUpResponse, SignUpRequest
from api.app.helper.base_response import DataResponse
from api.app.helper.db import db_session
from api.app.service.auth import AuthService

auth_router = APIRouter()

@auth_router.post('/register', response_model=DataResponse[SignUpResponse])
def register(db: Session = Depends(db_session), *, request: SignUpRequest):
    new_user = AuthService.create_new_user(db, request)
    return DataResponse().success_response(data=new_user)

