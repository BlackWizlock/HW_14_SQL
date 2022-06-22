from flask import Blueprint, jsonify
from .DAO.dbDao import Database

DB = Database(database="database/netflix.db")

bp = Blueprint("views", __name__)


@bp.route('/')
def index():
    return "Server - Running"


@bp.route('/movie/<string:title>')
def title_page(title: str):
    db_result = DB.search_title(title=title)
    return jsonify(db_result)


@bp.route('/movie/<int:year_first>/to/<int:year_second>')
def year_page(year_first: int, year_second: int):
    db_result = DB.search_year(year_first=year_first, year_second=year_second)
    return jsonify(db_result)


@bp.route('/rating/<string:rating>')
def rating_page(rating: str):
    db_result = []
    if rating == "children":
        db_result = DB.search_rating(rating="('G')")
    elif rating == "family":
        db_result = DB.search_rating(rating="('G', 'PG', 'PG-13')")
    elif rating == "adult":
        db_result = DB.search_rating(rating="('R', 'NC-17')")
    else:
        pass
    return jsonify(db_result)


@bp.route('/genre/<string:genre>')
def genre_page(genre: str):
    db_result = DB.search_genre(genre=genre)
    return jsonify(db_result)
