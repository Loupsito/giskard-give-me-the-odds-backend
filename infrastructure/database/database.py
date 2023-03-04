from databases import Database


class DatabaseHandler:
    database_engine: Database = None

    async def get_database(self, new_url: str = "sqlite:///./universe.db"):
        print("get_database")
        if self.database_engine is None:
            print("new get_database instance !")
            self.database_engine = Database("sqlite:///./" + new_url)
            await self.database_engine.connect()

        return self.database_engine
