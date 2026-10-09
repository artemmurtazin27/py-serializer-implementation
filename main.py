from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    serializer = CarSerializer(data=json)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
