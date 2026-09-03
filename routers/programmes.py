from fastapi import APIRouter, HTTPException
from database import engine
from sqlalchemy import text

# Initialise API router
router = APIRouter(
    # Add common path for all routes
    prefix="/programmes"
)

@router.get("")
async def read_programmes():
    # To be done: Retrieve programmes and apply filters
    return

@router.get("/{id}")
async def read_programme(id: int):
    # Retrieve a single programme in detail
    async with engine.connect() as conn:
        # SQL query to fetch the programme by ID
        query = text("SELECT * FROM programmes WHERE programme_id = :id")
        result = await conn.execute(query, {"id": id})
        
        # Get the first row as a dictionary
        programme = result.mappings().first()
        
        if not programme:
            raise HTTPException(status_code=404, detail="Programme not found")
            
        # Return the dictionary directly, FastAPI will serialize it to JSON
        return dict(programme)