from fastapi import APIRouter, Depends, HTTPException
from database import engine
from sqlalchemy import select
from metadata import get_metadata

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
async def read_programme(id: int, tables: dict = Depends(get_metadata)):

    # Retrieve a single programme in detail
    async with engine.connect() as conn:
        # SQL query to fetch the programme by ID
        query = select(tables["programmes"]).where(tables["programmes"].c.programme_id == id)
        result = await conn.execute(query, {"id": id})
        
        # Get the first row as a dictionary
        programme = result.mappings().first()
        
        if not programme:
            raise HTTPException(status_code=404, detail="Programme not found")
            
        # Return the dictionary directly, FastAPI will serialize it to JSON
        return dict(programme)