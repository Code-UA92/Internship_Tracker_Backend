from contextlib import asynccontextmanager
from fastapi import FastAPI
from metadata import load_tables
from routers import programmes

# Use lifespan to load tables at the start of the application
@asynccontextmanager
async def lifespan (app: FastAPI):
    # Start of application
    await load_tables()

    yield


# Initialise fastapi 
app = FastAPI(lifespan = lifespan)

# Add routers
app.include_router(programmes.router)