from flask import (
    jsonify,
    request
)

from models import (
    Farmer,
    Polygon,
    Weather
)

from .base import APIView


class PolygonView(APIView):

    def get(self):
        return {
            'type': "FeatureCollection",
            'features': [ feature.format(leaflet=True) for feature in Polygon.query.all() ]
        }

    def post(self):
        feature: dict = request.get_json() # type: ignore
        area: float = feature['properties'].get('area')
        farmer_name: str = feature['properties'].get('farmer')
        farmer: Farmer = Farmer.query.filter(Farmer.name == farmer_name).first()
        if farmer is None:
            farmer = Farmer(name=farmer_name)
            farmer.save()
        polygon: Polygon = Polygon(
            area=area,
            farmer_id=farmer.id
        )
        polygon.geometry_to_wkb(feature.get('geometry')) # type: ignore
        polygon.save()
        print(feature)
        return jsonify({
            'message': "CREATED"
        }), 201


class PolygonDataView(APIView):

    decorators: list = []

    def post(self):
        from datetime import date
        from json import load

        from lib.weather import weather_calculate

        data: dict = request.get_json() #type: ignore
        polygon_id: int = data['polygon_id']
        weather: Weather = Weather.query.filter(Weather.polygon_id == polygon_id).first()
        if weather is None:
            polygon_db: Polygon = Polygon.query.get(polygon_id).format()
            polygon: dict = {
                'geometry': polygon_db['geometry']['coordinates'][0]
            }
            data: dict = weather_calculate(polygon)
            weather = Weather(
                polygon_id=polygon_id,
                date=date(2022, 6, 2),
                temperature=data['temperature']
            )
            weather.save()
        with open("ndvi.json", "r", encoding="utf-8") as file:
            ndvi: dict = load(file)
        ndvi_data: list = []
        for item in ndvi:
            if item['id'] == polygon_id:
                ndvi_data = [
                    {'Suv va boshqa yerlar': item['T1']},
                    {'Ochiq yer maydon': item['T2']},
                    {'Kuchsiz rivojlangan': item['T3']},
                    {'O\'rtacha rivojlangan': item['T4']},
                    {'Yaxshi rivojlangan': item['T5']},
                    {'Juda yaxshi rivojlangan': item['T6']}
                ]
        return jsonify({
            'data': {
                'temperature': weather.temperature,
                'ndvi': ndvi_data
            }
        })
