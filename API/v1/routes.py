from fastapi import APIRouter, HTTPException, status,Query # type: ignore
from pydantic import BaseModel
from datetime import timedelta
from core.utils import hash_password,verify_password,create_access_token
from core.db import get_user_by_username, add_user
from services.stt_service import handle_speak
from fastapi.responses import RedirectResponse # type: ignore

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password:str
    
class RegisterRequest(BaseModel):
    username:str
    email:str
    password:str
    
class AuthResponse(BaseModel):
    message:str
    token: str = None
    
@router.post("/register", response_model = AuthResponse) 
def register_user(user:RegisterRequest):
    existing_user = get_user_by_username(user.username)
    if existing_user:
        raise HTTPException(
            status_code = status.HTTP_404_BAD_REQUEST,
            detail = "Username already exists"
        )
    
    hased_password = hash_password(user.password)
    
    add_user(user.username, user.email,hased_password)
    
    return RedirectResponse(url='/login',status_code=303)

@router.post("/login",response_model = AuthResponse)
def login_user(user:LoginRequest):
    db_user = get_user_by_username(user.username)
    access_token = create_access_token(data={"sub":user.username})
    if not db_user or not verify_password(user.password,db_user["hashed_password"]):
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    else:
        return RedirectResponse(url="/home",status_code=303)        
    
@router.get("/home")
def home_page():
    return {"message":"welcome to AI Study Buddy APP"}   


language_options ={
    "en":"English",
    "te":"Telugu",
    "hi":"Hindi",
    "ta":"Tamil",
    "kn":"Kannada",
    "ml":"Malayalam"
}
@router.get("/speak")
def speak(language:str =  Query("en",title="select language",description ="Choose a spoken language",enum=list(language_options.keys())),language2:str=Query("en",title="select language",description ="Choose a spoken language",enum=list(language_options.keys()))):
    return handle_speak(language,language2)
        
    