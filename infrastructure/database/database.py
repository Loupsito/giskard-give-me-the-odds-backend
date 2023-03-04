from databases import Database


class DatabaseHandler:
    database_engine: Database = None

    async def get_database(self, new_url: str = "sqlite:///./universe.db"):
        if self.database_engine is None:
            self.database_engine = Database("sqlite:///./" + new_url)
            await self.database_engine.connect()

        return self.database_engine
