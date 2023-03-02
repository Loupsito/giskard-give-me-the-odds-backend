from databases import Database

from app_module import app

database_engine = Database("sqlite:///./universe.db")


@app.on_event("startup")
async def database_connect():
    await database_engine.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database_engine.disconnect()
