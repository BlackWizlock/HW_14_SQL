from dataclasses import dataclass
import hwapp.models.DAO.dbDao as dbDao

DB = dbDao.Database(database="database/netflix.db")


@dataclass
class SearchGenreReport:
    title: str
    description: str


class GetGenreService:
    @staticmethod
    def _get_data_from_db(genre):
        return DB.search_genre(genre)

    def execute(self, genre: str) -> SearchGenreReport:
        for row in self._get_data_from_db(genre):
            yield SearchGenreReport(
                    title=row[0],
                    description=row[1]
            )
