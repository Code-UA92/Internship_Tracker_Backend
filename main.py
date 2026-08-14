from fastapi import FastAPI
from routers import programmes

# Initialise fastapi 
app = FastAPI()

# Add routers
app.include_router(programmes.router)