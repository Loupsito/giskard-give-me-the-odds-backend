async def get_all_routes(db):
    query = "SELECT * from routes"
    return await db.fetch_all(query=query)
