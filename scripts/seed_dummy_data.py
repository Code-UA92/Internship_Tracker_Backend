import asyncio
from sqlalchemy import MetaData, insert
from faker import Faker
from random import randint

from database import engine

async def main():
    # Initialise faker 
    fake = Faker('en_gb')

    # Populate companies table
    companies = []
    for _ in range(30):
        company = {
            "name": fake.company(),
            "job_board_site": fake.url()
        }
        companies.append(company)

    # Populate locations table
    location_names = ["London", "Manchester", "Birmingham", "Edinburgh", "Glasgow", "Bristol", "Leeds", "Remote"]
    locations = [{"name": loc} for loc in location_names]

    # Populate types table
    type_names = ["Apprenticeship", "Graduate Scheme", "Summer Internship", "Placement Year"]
    types = [{"name": t} for t in type_names]

    # Populate programmes table
    programmes = []
    for _ in range(100):
        programme = {
            "company_id": randint(1, len(companies)), 
            "type_id": randint(1, len(type_names)),
            "locations_id": randint(1, len(location_names)),
            "title": f"{fake.job()} Programme",
            "description": fake.paragraph(nb_sentences=3),
            "qualifications": fake.paragraph(nb_sentences=2),
            "preferred_qualifications": fake.paragraph(nb_sentences=2),
            "deadline": fake.date_between(start_date='today', end_date='+1y')
        }
        programmes.append(programme)


    metadata = MetaData()

    async with engine.begin() as conn:

        await conn.run_sync(
            metadata.reflect,
            only=['companies', 'locations', 'types', 'programmes']
        )

        # Extract table objects from the reflected metadata
        companies_table = metadata.tables['companies']
        locations_table = metadata.tables['locations']
        types_table = metadata.tables['types']
        programmes_table = metadata.tables['programmes']
     
        # Insert data using the extracted table objects
        await conn.execute(insert(companies_table), companies)
        await conn.execute(insert(locations_table), locations)
        await conn.execute(insert(types_table), types)
        await conn.execute(insert(programmes_table), programmes)

        print("All dummy data has been inserted!")

if __name__ == "__main__":
    asyncio.run(main())