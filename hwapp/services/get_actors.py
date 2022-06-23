from dataclasses import dataclass

import hwapp.models.DAO.dbDao as dbDao

DB = dbDao.Database(database="database/netflix.db")


@dataclass
class SearchActorsReport:
    cast: str


class GetActorsService:
    @staticmethod
    def _get_data_from_db(actor1: str, actor2: str):
        return DB.search_actors(actor1, actor2)

    def execute(self, actor1: str, actor2: str) -> SearchActorsReport:
        db_response = self._get_data_from_db(actor1, actor2)
        if len(db_response) >= 2:
            for row in db_response:
                yield SearchActorsReport(
                        cast=row[0]
                )
