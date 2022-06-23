from dataclasses import dataclass
import hwapp.models.DAO.dbDao as dbDao

DB = dbDao.Database(database="database/netflix.db")


@dataclass
class SearchAllReport:
    title: str
    description: str


class GetAllService:
    @staticmethod
    def _get_data_from_db(type_movie: str, release_year: int, listed_in: str):
        return DB.search_all(type_movie, release_year, listed_in)

    def execute(self, genre: str) -> SearchAllReport:
        for row in self._get_data_from_db(genre):
            yield SearchAllReport(
                    title=row[0],
                    description=row[1]
            )
