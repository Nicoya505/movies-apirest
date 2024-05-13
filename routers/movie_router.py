from shemas import MovieShema
from services import MovieService
from config import Session

from typing import List

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import Path, Query, Body, status

movie_router = APIRouter()

@movie_router.post(
    "/movie",
    status_code=status.HTTP_201_CREATED,
    tags=["Movies"],
    response_model=dict
)
def create_movie(movie: MovieShema = Body(...)):
    session = Session()
    MovieService(session).create_movie(movie)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message":"successfully created movie"})


@movie_router.get(
    "/movie",
    status_code=status.HTTP_200_OK,
    tags=["Movies"],
    response_model=List[MovieShema]
)
def get_movies():
    session = Session()
    movies = MovieService(session).get_movies()
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(movies))


@movie_router.get(
    "/movie/{id}",
    status_code=status.HTTP_200_OK,
    tags=["Movies"],
    response_model=MovieShema
)
def get_movie_by_id(id: int = Path(..., ge=1)):
    session = Session()
    movie = MovieService(session).get_movie_by_id(id)

    if not movie:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": "movie not found"})
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(movie))


@movie_router.get(
    "/movie/",
    status_code=status.HTTP_200_OK,
    tags=["Movies"],
    response_model=List[MovieShema]
)
def get_movie_by_category(category: str = Query(..., min_length=5, max_length=50)):
    session = Session()
    movies = MovieService(session).get_movie_by_category(category)

    if not movies:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": "movie not found"})
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(movies))


@movie_router.put(
    "/movie/{id}",
    status_code=status.HTTP_200_OK,
    tags=["Movies"],
    response_model=dict
)
def update_movie(id: int = Path(..., ge=1), movie: MovieShema = Body(...)):
    session = Session()
    data = MovieService(session).get_movie_by_id(id)

    if not data:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": "movie not found"})
    
    MovieService(session).update_movie(id, movie)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message":"successfully update movie"})



@movie_router.delete(
    "/movie/{id}",
    status_code=status.HTTP_200_OK,
    tags=["Movies"],
    response_model=dict
)
def delete_movie(id: int = Path(..., ge=1)):
    session = Session()
    movie = MovieService(session).get_movie_by_id(id)

    if not movie:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": "movie not found"})
    
    MovieService(session).delete_movie(id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message":"successfully delete movie"})