from passlib.context import CryptContext # type: ignore
from jose import JWTError, jwt # type: ignore
from datetime import datetime,timedelta
from core.config import SECRET_KEY,ALGORITHM,ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(palin_password:str,hased_password:str):
    return pwd_context.verify(palin_password,hased_password)

def create_access_token(data:dict,expires_delta:timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.utcnow()+expires_delta
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt