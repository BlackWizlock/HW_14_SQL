import sqlite3


class Database:
    def __init__(self, database: str, table_name: str = 'netflix') -> None:
        self.database = database
        self.table_name = table_name

    def _database_connection(self):
        """ Подключаем БД SQL, активируем row_factory """
        with sqlite3.connect(self.database) as con:
            con.row_factory = sqlite3.Row
            cursor = con.cursor()
        return cursor

    def search_title(self, title: str):
        """ Метод класса по поиску названия фильма """
        cursor = self._database_connection()
        sqlite_query = f"""
            SELECT title, country, release_year, listed_in, description 
            FROM {self.table_name}
            WHERE title LIKE :substring
            """
        cursor.execute(sqlite_query, {"substring": f"%{title}%"})
        db_results = cursor.fetchall()
        result = []
        for row in db_results:
            result.append(
                    {
                            'title'       : row['title'],
                            'country'     : row['country'],
                            'release_year': row['release_year'],
                            'genre'       : row['listed_in'],
                            'description' : row['description'].strip()
                    }
            )
        return result

    def search_year(self, year_first: int, year_second: int):
        cursor = self._database_connection()
        sqlite_query = f"""
                            SELECT title, release_year 
                            FROM {self.table_name}
                            WHERE release_year BETWEEN :substring_year_first AND :substring_year_second
                            ORDER BY release_year DESC 
                            LIMIT 100
                        """
        cursor.execute(sqlite_query, {"substring_year_first" : f"{year_first}",
                                      "substring_year_second": f"{year_second}"})
        db_results = cursor.fetchall()
        result = []
        for row in db_results:
            result.append(
                    {
                            'title'       : row['title'],
                            'release_year': row['release_year']
                    }
            )
        return result

    def search_rating(self, rating: str):
        cursor = self._database_connection()
        sqlite_query = """
                    SELECT title, rating, description
                    FROM {self.table_name}
                    WHERE rating IN :substring_rating
                """
        cursor.execute(sqlite_query, {"substring_rating": f"{rating}"})
        db_results = cursor.fetchall()
        result = []
        for row in db_results:
            result.append(
                    {
                            'title'      : row['title'],
                            'rating'     : row['rating'],
                            'description': row['description'].strip()
                    }

            )
        return result


def search_genre(self, genre: str):
    cursor = self._database_connection()
    sqlite_query = f"""
                        SELECT title, description
                        FROM {self.table_name}
                        WHERE listed_in LIKE :substring_genre
                        ORDER BY release_year DESC
                        LIMIT 10;
                    """
    cursor.execute(sqlite_query, {"substring_genre": f"%{genre}%"})
    db_results = cursor.fetchall()
    result = []
    for row in db_results:
        result.append(
                {
                        'title'      : row['title'],
                        'description': row['description'].strip()
                }
        )
    return result
