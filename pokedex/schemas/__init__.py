from schematics import Model
from schematics.types import StringType


class Movie(Model):
    name = StringType(required=True)
    image = StringType(required=True)
    title = StringType(required=True)
    description = StringType(required=True)
    year = StringType(required=True)
