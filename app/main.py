from fastapi import FastAPI
from .database import engine, Base
from .routers import items

# Create all tables defined by classes that inherit from Base
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Item Management API")

# Include the items router so its endpoints are added to the app
app.include_router(items.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Item API"}