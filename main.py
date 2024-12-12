from fastapi import FastAPI, HTTPException

app = FastAPI()

Bands = [
    {'id': 1, 'name': 'The Kinks', 'genre': 'Rock'},
    {'id': 2, 'name': 'Aphex Twin', 'genre': 'Electronic'},
    {'id': 3, 'name': 'Slowdive', 'genre': 'Shoegaze'},
    {'id': 4, 'name': 'Wu-Tang Clan', 'genre': 'Hip-Hop'},
]

@app.get('/bands')
async def bands() -> list[dict]:
    return Bands

@app.get('/bands/{band_id}')
async def band(band_id: int) -> dict:
    band = next((b for b in Bands if b['id'] == band_id), None)
    if band is None:
        # status 404
        raise HTTPException(status_code=404, detail='band not found')
    return band
