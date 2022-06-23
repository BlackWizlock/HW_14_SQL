from dataclasses import dataclass
import hwapp.models.DAO.dbDao as dbDao

DB = dbDao.Database(database="database/netflix.db")


@dataclass
class SearchYearReport:
    title: str
    release_year: int


class GetYearService:
    @staticmethod
    def _get_data_from_db(year_first, year_second):
        return DB.search_year(year_first, year_second)

    def execute(self, year_first: int, year_second: int) -> SearchYearReport:
        for row in self._get_data_from_db(year_first, year_second):
            yield SearchYearReport(
                    title=row[0],
                    release_year=row[1]
            )
