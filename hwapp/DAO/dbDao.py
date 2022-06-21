import sqlite3
from flask import jsonify


class Database:
    def __init__(self, database: str, table_name: str = 'netflix') -> None:
        self.database = database
        self.table_name = table_name

    def _database_connection(self, query_string: str):
        with sqlite3.connect(self.database) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            result = cur.execute(query_string)
            data_flow = result.fetchall()
        return data_flow

    def search_title(self, title: str):
        output = self._database_connection(
                f"""SELECT 
                        title, 
                        country, 
                        release_year, 
                        listed_in, 
                        description 
                    FROM {self.table_name}
                    WHERE title LIKE '%{title}%'
                """)
        result = []
        for row in output:
            result.append(
                    {
                            'title'       : row['title'],
                            'country'     : row['country'],
                            'release_year': row['release_year'],
                            'genre'   : row['listed_in'],
                            'description' : row['description'].strip()
                    }
            )
        return jsonify(result)

    def search_year(self, year_first: int, year_second: int):
        output = self._database_connection(
                f"""SELECT 
                        title, 
                        release_year 
                    FROM {self.table_name}
                    WHERE release_year BETWEEN {year_first} AND {year_second}
                    ORDER BY release_year DESC 
                    LIMIT 100
                """)
        result = []
        for row in output:
            result.append(
                    {
                            'title'       : row['title'],
                            'release_year': row['release_year']
                    }
            )
        return jsonify(result)

    def search_rating(self, rating: str):
        output = self._database_connection(
                f"""SELECT
                        title,
                        rating,
                        description
                    FROM {self.table_name}
                    WHERE rating IN {rating};
                """)
        result = []
        for row in output:
            result.append(
                    {
                            'title'      : row['title'],
                            'rating'     : row['rating'],
                            'description': row['description'].strip()
                    }
            )
        return jsonify(result)

    def search_genre(self, genre: str):
        output = self._database_connection(
                f"""SELECT
                                title,
                                description
                            FROM {self.table_name}
                            WHERE listed_in LIKE '%{genre}%'
                            ORDER BY release_year DESC
                            LIMIT 10;
                        """)
        result = []
        for row in output:
            result.append(
                    {
                            'title'      : row['title'],
                            'description': row['description'].strip()
                    }
            )
        return jsonify(result)
