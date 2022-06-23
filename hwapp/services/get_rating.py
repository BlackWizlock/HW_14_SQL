from dataclasses import dataclass
import hwapp.models.DAO.dbDao as dbDao

DB = dbDao.Database(database="database/netflix.db")


@dataclass
class SearchRatingReport:
    title: str
    rating: str
    description: str


RATING_REQUEST = {
        "children": "'G',",
        "family"  : "('G', 'PG', 'PG-13')",
        "adult"   : "('R', 'NC-17')"
}


class GetRatingService:
    @staticmethod
    def _get_data_from_db(rating):
        return DB.search_rating(RATING_REQUEST[rating])

    def execute(self, rating: str) -> SearchRatingReport:
        for row in self._get_data_from_db(rating):
            yield SearchRatingReport(
                    title=row[0],
                    rating=row[1],
                    description=row[2]
            )
