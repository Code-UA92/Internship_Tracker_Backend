from fastapi import APIRouter

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
    # To be done: Retrieve a single programme in detail
    return