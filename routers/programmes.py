from fastapi import APIRouter, Depends, HTTPException, Query
from database import engine
from sqlalchemy import select, func
from metadata import get_metadata

# Initialise API router
router = APIRouter(
    # Add common path for all routes
    prefix="/programmes"
)

@router.get("/all")
async def read_programmes(
    skip: int = Query(0, description= "Skip"),
    limit: int = Query(10, ge=1, description="Programmes per page"),
    tables: dict = Depends(get_metadata)
):
    async with engine.connect() as conn:
        #For getting paginated programmes
        query = select(tables["programmes"]).offset(skip).limit(limit)
        result = await conn.execute(query)
        programmes = result.mappings().all()

        #For getting total programmes
        count_programmes = select(func.count()).select_from(tables["programmes"])
        count_result = await conn.execute(count_programmes)
        total_programmes = count_result.scalar()

        #For getting total pages
        total_pages = (total_programmes + limit - 1) // limit
    return {
        "items": [dict(p) for p in programmes],
        "skip": skip,
        "limit": limit,
        "total_programmes": total_programmes,
        "total_pages": total_pages,
        "has_next": skip +limit < total_programmes,
        "has_prev": skip > 0
    }

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