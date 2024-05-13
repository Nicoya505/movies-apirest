from shemas import MovieShema
from models import MovieModel

class MovieService:
    def __init__(self, session):
        self.session = session

    
    def create_movie(self, movie: MovieShema):
        new_movie = MovieModel(**movie.model_dump())
        self.session.add(new_movie)
        self.session.commit()
        return 
    
    
    def get_movies(self):
        new_movies = self.session.query(MovieModel).all()
        return new_movies
    

    def get_movie_by_id(self, id: int):
        new_movie = self.session.query(MovieModel).filter(MovieModel.id == id).first()
        return new_movie
    

    def get_movie_by_category(self, category: str):
        new_movies = self.session.query(MovieModel).filter(MovieModel.category == category).all()
        return new_movies
    

    def update_movie(self, id: int, movie: MovieShema ):
        data = self.session.query(MovieModel).filter(MovieModel.id == id).first()
        data.title = movie.title
        data.category = movie.category
        data.year = movie.year

        self.session.commit()
        return
    
    
    def delete_movie(self, id:int ):
        self.session.query(MovieModel).filter(MovieModel.id == id).delete()
        self.session.commit()
