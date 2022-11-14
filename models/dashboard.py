from dataclasses import dataclass
from geoalchemy2 import Geometry

from extensions import db

from .auth import Profile
from .base import (
    BaseModel,
    TimestampMixin
)


@dataclass
class Farmer(BaseModel):

    __tablename__: str = "farmer"

    name = db.Column(db.String(255))

    polygons = db.relationship("Polygon", backref="farmer")

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


@dataclass(init=False)
class Polygon(BaseModel, TimestampMixin):

    __tablename__: str = "polygon"

    profile: Profile
    farmer: Farmer
    name = db.Column(db.String(120), default="Yangi maydon")
    geometry = db.Column(Geometry(geometry_type="POLYGON", srid=4326))
    area = db.Column(db.Float)
    farmer_id = db.Column(db.Integer, db.ForeignKey("farmer.id", ondelete="CASCADE"))
    profile_id = db.Column(db.Integer, db.ForeignKey("auth_profile.id", ondelete="CASCADE"))

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name

    def geometry_to_wkb(self, geometry: dict) -> None:
        from geomet.wkt import dumps

        self.geometry = dumps(geometry)
    
    def format(self, leaflet: bool = False) -> dict:
        from geoalchemy2.functions import ST_AsGeoJSON
        from json import loads

        geometry: dict = loads(db.session.query(ST_AsGeoJSON(Polygon.geometry)).filter(Polygon.id == self.id).first()[0])
        if leaflet:
            geometry = {
                'coordinates': [[ [item[1], item[0]] for item in geometry['coordinates'][0] ]],
                **{ k: v for k, v in geometry.items() if k != "coordinates" }
            }
        return {
            'type': "Feature",
            'geometry': geometry,
            'properties': {
                'farmer_name': self.farmer.name,
                **{ k: v for k, v in self.__dict__.items() if not (k in ["geometry"] or k.startswith("_")) }
            }
        }


class Weather(BaseModel):

    __tablename__: str = "weather"

    polygon: Polygon
    polygon_id = db.Column(db.Integer, db.ForeignKey("polygon.id", ondelete="CASCADE"))
    date = db.Column(db.Date)
    temperature = db.Column(db.Float)


    def __repr__(self) -> str:
        return self.polygon.name - self.date

    def __str__(self) -> str:
        return self.polygon.name - self.date


class Tile(BaseModel):

    __tablename__: str = "tile"

    polygon: Polygon
    polygon_id = db.Column(db.Integer, db.ForeignKey("polygon.id", ondelete="CASCADE"))
    type = db.Column(db.String(10))
    date = db.Column(db.Date())
    file = db.Column(db.String(255))

    def __repr__(self) -> str:
        return self.file
    
    def __str__(self) -> str:
        return self.file
