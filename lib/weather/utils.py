from requests import request
from shapely.geometry import Polygon


def weather_calculate(polygon: dict) -> dict:
    new_polygon: Polygon = Polygon(polygon['geometry'])
    center = new_polygon.centroid.coords[0]
    lat, lng = center
    rq = request(
        method="GET",
        url="https://archive-api.open-meteo.com/v1/era5",
        params={
            'latitude': lat,
            'longitude': lng,
            'start_date': "2022-06-02",
            'end_date': "2022-06-02",
            'hourly': "temperature_2m",
            'timezone': "Asia/Tashkent"
        }
    )
    response_data: dict = rq.json()
    return_data: dict = {}
    for key, value in response_data['hourly'].items():
        if key != 'time':
            data: float = 0
            for item in value:
                data += item
            return_data[key.split("_")[0]] = data / len(value)
    return return_data
