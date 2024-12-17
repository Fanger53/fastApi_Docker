from datetime import date
from enum import Enum
from pydantic import BaseModel, validator


class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HIP_HOP = 'hip-hop'


class GenreChoices(Enum):
    ROCK = 'Rock'
    ELECTRONIC = 'Electronic'
    METAL = 'Metal'
    HIP_HOP = 'Hip-hop'


class Album(BaseModel):
    title: str
    release: date


class Band(BaseModel):
    id: int
    name: str
    genre: GenreChoices
    album: list[Album] = []  # default response


class BandBase(BaseModel):
    name: str
    genre: str
    albums: list[Album] = []


class BandCreate(BandBase):
    @validator('genre', pre=True)
    def title_genre_case(cls, value):
        return value.title()


class BandWithId(BandBase):
    id: int
