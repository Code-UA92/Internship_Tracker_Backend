from sqlalchemy import MetaData
from database import engine

# Initialise Metadata object
metadata_obj = MetaData()

# Load table schema to MetaData from pre-exisiting database
async def load_tables():
    async with engine.connect() as conn:
        # Run reflection code synchronusly
        # Reflection can't be run asynchronusly
        await conn.run_sync(metadata_obj.reflect)

async def get_metadata():
    return metadata_obj.tables
