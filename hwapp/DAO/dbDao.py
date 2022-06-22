import sqlite3


class Database:
    def __init__(self, database: str) -> None:
        self.database = database

    def _database_connection(self):
        """ Подключаем БД SQL, активируем row_factory """
        with sqlite3.connect(self.database) as con:
            con.row_factory = sqlite3.Row
            cursor = con.cursor()
        return cursor

    def search_title(self, title: str):
        """ Поиск фильмов по вхождению в название """
        cursor = self._database_connection()
        sqlite_query = f"""
            SELECT title, country, release_year, listed_in, description 
            FROM netflix
            WHERE title LIKE :substring
            """
        cursor.execute(sqlite_query, {"substring": f"%{title}%"})
        return cursor.fetchall()

    def search_year(self, year_first: int, year_second: int):
        """ Поиск между двумя годами """
        cursor = self._database_connection()
        sqlite_query = f"""
                            SELECT title, release_year 
                            FROM netflix
                            WHERE release_year BETWEEN :substring_year_first AND :substring_year_second
                            ORDER BY release_year DESC 
                            LIMIT 100
                        """
        cursor.execute(sqlite_query, {"substring_year_first" : f"{year_first}",
                                      "substring_year_second": f"{year_second}"})
        return cursor.fetchall()

    def search_rating(self, rating: str):
        """ Поиск по рейтингу """
        cursor = self._database_connection()
        sqlite_query = f"""
                            SELECT title, rating, description
                            FROM netflix
                            WHERE rating IN :substring_rating
                """
        cursor.execute(sqlite_query, {"substring_rating": f"{rating}"})
        return cursor.fetchall()

    def search_genre(self, genre: str):
        """ Поиск по жанру """
        cursor = self._database_connection()
        sqlite_query = f"""
                            SELECT title, description
                            FROM netflix
                            WHERE listed_in LIKE :substring_genre
                            ORDER BY release_year DESC
                            LIMIT 10;
                        """
        cursor.execute(sqlite_query, {"substring_genre": f"%{genre}%"})
        return cursor.fetchall()
