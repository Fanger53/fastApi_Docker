from fastapi import FastAPI, HTTPException, Path, Query
from schema import GenreURLChoices, BandCreate, BandWithId
from typing import Annotated


app = FastAPI()


Bands = [
    {'id': 1, 'name': 'The Kinks', 'genre': 'Rock'},
    {'id': 2, 'name': 'Aphex Twin', 'genre': 'Electronic'},
    {'id': 3, 'name': 'Pantera', 'genre': 'Metal'},
    {'id': 4, 'name': 'Wu-Tang Clan', 'genre': 'Hip-Hop'},
]


@app.get('/bands')
async def bands(
    genre: GenreURLChoices | None = None,
    q: Annotated[str | None, Query(max_length=10)] = None,
) -> list[BandWithId]:
    band_list = [BandWithId(**b) for b in Bands]
    if genre:
        return [
            b for b in band_list if b.genre.value.lower() == genre.value
        ]
    
    if q:
        band_list = [
            b for b in band_list if q.lower() in b.name.lower()
        ]
    return band_list


@app.get('/bands/{band_id}', status_code=200)
async def band(
    band_id: Annotated[int,
    Path(title='the band id')]) -> BandWithId:
    band = next((BandWithId(**b) for b in Bands if b['id'] == band_id), None)
    if band is None:
        # status 404
        raise HTTPException(status_code=404, detail='band not found')
    return band


@app.get('/bands/genre/{genre}', status_code=200)
async def band_for_genre(genre: GenreURLChoices) -> list[dict]:
    return [
        b for b in Bands if b['genre'].lower() == genre.value
    ]


@app.post('/bands', status_code=200)
async def create_band(band_data: BandCreate) -> BandWithId:
    id = Bands[-1]["id"] + 1
    band = BandWithId(id=id, **band_data.model_dump()).model_dump()
    Bands.append(band)
    return band
