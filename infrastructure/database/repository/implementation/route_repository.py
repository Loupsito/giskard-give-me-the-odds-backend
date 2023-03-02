from infrastructure.database.database import database_engine


async def get_all_routes():
    query = "SELECT * from routes"
    return await database_engine.fetch_all(query=query)
