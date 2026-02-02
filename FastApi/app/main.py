from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime, timedelta
import jwt
from passlib.context import CryptContext

# Configuration
SECRET_KEY = "your-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Initialize FastAPI app
app = FastAPI(title="Simple FastAPI with Auth", version="1.0.0")

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Security
security = HTTPBearer()

# In-memory databases (replace with real database in production)
users_db = {}
items_db = []


# Models
class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: Optional[str] = None


class UserLogin(BaseModel):
    username: str
    password: str


class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    disabled: bool = False


class Token(BaseModel):
    access_token: str
    token_type: str


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    owner: Optional[str] = None
    created_at: Optional[datetime] = None


# Helper functions
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired"
        )
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> User:
    token = credentials.credentials
    payload = decode_token(token)
    username = payload.get("sub")

    if username is None or username not in users_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )

    user_data = users_db[username]
    return User(**user_data)


# Routes
@app.get("/")
def root():
    return {
        "message": "Welcome to FastAPI with Authentication",
        "endpoints": {
            "register": "POST /auth/register",
            "login": "POST /auth/login",
            "me": "GET /auth/me (protected)",
            "items": "GET /items (protected)",
            "create_item": "POST /items (protected)",
            "get_item": "GET /items/{item_id} (protected)",
            "update_item": "PUT /items/{item_id} (protected)",
            "delete_item": "DELETE /items/{item_id} (protected)",
        },
    }


# Authentication endpoints
@app.post("/auth/register", response_model=User, status_code=status.HTTP_201_CREATED)
def register(user: UserRegister):
    if user.username in users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )

    hashed_password = hash_password(user.password)
    user_data = {
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name,
        "hashed_password": hashed_password,
        "disabled": False,
    }
    users_db[user.username] = user_data

    return User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        disabled=False,
    )


@app.post("/auth/login", response_model=Token)
def login(user_login: UserLogin):
    if user_login.username not in users_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    user_data = users_db[user_login.username]
    if not verify_password(user_login.password, user_data["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    access_token = create_access_token(data={"sub": user_login.username})
    return Token(access_token=access_token, token_type="bearer")


@app.get("/auth/me", response_model=User)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user


# CRUD endpoints for items (protected)
@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item, current_user: User = Depends(get_current_user)):
    new_item = item.dict()
    new_item["id"] = len(items_db) + 1
    new_item["owner"] = current_user.username
    new_item["created_at"] = datetime.utcnow()
    items_db.append(new_item)
    return new_item


@app.get("/items", response_model=List[Item])
def get_items(current_user: User = Depends(get_current_user)):
    # Return only items owned by current user
    user_items = [item for item in items_db if item["owner"] == current_user.username]
    return user_items


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int, current_user: User = Depends(get_current_user)):
    for item in items_db:
        if item["id"] == item_id:
            if item["owner"] != current_user.username:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Not authorized to access this item",
                )
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@app.put("/items/{item_id}", response_model=Item)
def update_item(
    item_id: int, item_update: Item, current_user: User = Depends(get_current_user)
):
    for idx, item in enumerate(items_db):
        if item["id"] == item_id:
            if item["owner"] != current_user.username:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Not authorized to update this item",
                )
            updated_item = item.copy()
            updated_item.update(
                {
                    "name": item_update.name,
                    "description": item_update.description,
                    "price": item_update.price,
                }
            )
            items_db[idx] = updated_item
            return updated_item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, current_user: User = Depends(get_current_user)):
    for idx, item in enumerate(items_db):
        if item["id"] == item_id:
            if item["owner"] != current_user.username:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Not authorized to delete this item",
                )
            items_db.pop(idx)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
