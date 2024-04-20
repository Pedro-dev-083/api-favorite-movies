"""Módulo de inicialização dos schemas"""

from schemas.movie import MovieSchema, MovieViewSchema, MovieUpdateSchema, ListMoviesSchema, show_movie, show_movies
from schemas.genre import GenreSchema, GenreViewSchema, ListGenresSchema, show_genre, show_genres
from schemas.error import ErrorSchema
from schemas.generic import IdSchema, GenericSchema
