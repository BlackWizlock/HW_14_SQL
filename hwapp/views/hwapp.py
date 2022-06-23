from flask import Blueprint, jsonify
from hwapp.services.get_title_movie import GetTitleMovieService
from hwapp.services.get_year import *
from hwapp.services.get_rating import *
from hwapp.services.get_genre import *
from hwapp.services.get_actors import *
from hwapp.services.get_all import *


bp = Blueprint("views", __name__)


@bp.route('/')
def index():
    return "Server - Running"


@bp.route('/movie/<string:title>')
def title_page(title: str):
    return jsonify(list(GetTitleMovieService().execute(title)))


@bp.route('/movie/<int:year_first>/to/<int:year_second>')
def year_page(year_first: int, year_second: int):
    return jsonify(list(GetYearService().execute(year_first, year_second)))


@bp.route('/genre/<string:genre>')
def genre_page(genre: str):
    return jsonify(list(GetGenreService().execute(genre)))


@bp.route('/rating/<string:rating>')
def rating_page(rating: str):
    return jsonify(list(GetRatingService().execute(rating)))


@bp.route('/cast/<string:actor1>/<string:actor2>')
def cast_page(actor1: str, actor2: str):
    return jsonify(list(GetActorsService().execute(actor1, actor2)))
