from dataclasses import dataclass
import hwapp.models.DAO.dbDao as dbDao

DB = dbDao.Database(database="database/netflix.db")


@dataclass
class SearchTitleReport:
    title: str
    country: str
    release_year: int
    listed_in: str
    description: str


class GetTitleMovieService:
    @staticmethod
    def _get_data_from_db(title):
        return DB.search_title(title)

    def execute(self, title: str) -> SearchTitleReport:
        for row in self._get_data_from_db(title):
            yield SearchTitleReport(
                    title=row[0],
                    country=row[1],
                    release_year=row[2],
                    listed_in=row[3],
                    description=row[4]
            )
