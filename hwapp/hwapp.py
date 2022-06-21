from flask import Blueprint, jsonify, request, render_template
from .DAO.dbDao import Database

DB = Database(database="database/netflix.db")

bp = Blueprint("views", __name__)


@bp.route('/')
def index():
    return "Server - Running"


@bp.route('/movie/<string:title>')
def title_page(title: str):
    return DB.search_title(title=title)


@bp.route('/movie/<int:year_first>/to/<int:year_second>')
def year_page(year_first: int, year_second: int):
    return DB.search_year(year_first=year_first, year_second=year_second)


@bp.route('/rating/<string:rating>')
def rating_page(rating: str):
    if rating == "children":
        return DB.search_rating(rating="('G')")
    elif rating == "family":
        return DB.search_rating(rating="('G', 'PG', 'PG-13')")
    elif rating == "adult":
        return DB.search_rating(rating="('R', 'NC-17')")


@bp.route('/genre/<string:genre>')
def genre_page(genre: str):
    return DB.search_genre(genre=genre)
