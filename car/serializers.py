from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(
        validators=[MaxValueValidator(1914), MinValueValidator(1)]
    )
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(null=True, blank=True)
