from weather import Weather
from spotify import Spotify
from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import zipcodes

app = FastAPI()


@app.get("/find-music-recs")
async def get_weather (
        zipcode: str = Header (
            None,
            alias="zipcode",
            description="User's zipcode"
        )
):
    if (
            zipcode is None or
            len(zipcode) != 5 or
            not zipcode.isnumeric() or
            not zipcodes.is_real(zipcode)
    ):
        raise HTTPException(status_code=400, detail="Invalid zipcode")


    try:

        weather = Weather(zipcode)
        spotify = Spotify()

        moods = weather.get_mood_keywords()
        search_results = spotify.search_music(moods)

        json_compatible_data = jsonable_encoder(search_results)

        return JSONResponse(
            content=json_compatible_data,
            status_code=200
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error occurred: {str(e)}"
        )

