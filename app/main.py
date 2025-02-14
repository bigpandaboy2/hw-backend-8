from fastapi import FastAPI
from app.routers import auth, flowers, cart

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(flowers.router, tags=["flowers"])
app.include_router(cart.router, prefix="/cart", tags=["cart"])