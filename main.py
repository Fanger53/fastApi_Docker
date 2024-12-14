from fastapi import FastAPI, HTTPException
from schema import GenreURLChoices, Band

app = FastAPI()


Bands = [
    {'id': 1, 'name': 'The Kinks', 'genre': 'Rock'},
    {'id': 2, 'name': 'Aphex Twin', 'genre': 'Electronic'},
    {'id': 3, 'name': 'Pantera', 'genre': 'Metal'},
    {'id': 4, 'name': 'Wu-Tang Clan', 'genre': 'Hip-Hop'},
]

@app.get('/bands')
async def bands(genre: GenreURLChoices | None = None) -> list[Band]:
    band_list = [Band(**b) for b in Bands]
    if genre:
        return [
            b for b in band_list if b.genre.lower() == genre.value
        ]
    return [
        Band(**b) for b in Bands
    ]

@app.get('/bands/{band_id}', status_code=200)
async def band(band_id: int) -> Band:
    band = next((Band(**b) for b in Bands if b['id'] == band_id), None)
    if band is None:
        # status 404
        raise HTTPException(status_code=404, detail='band not found')
    return band

@app.get('/bands/genre/{genre}', status_code=200)
async def band_for_genre(genre: GenreURLChoices) -> list[dict]:
    return [
        b for b in Bands if b['genre'].lower() == genre.value
    ]  
