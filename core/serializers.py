from rest_framework import serializers
from django.contrib.auth.models import User

from . import models


class CrewMember(serializers.ModelSerializer):
    class Meta:
        model = models.CrewMember
        fields = "__all__"
        read_only_fields = ["id"]


class Manufacturer(serializers.ModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = "__all__"
        read_only_fields = ["id"]


class Aircraft(serializers.ModelSerializer):
    manufacturer = Manufacturer(read_only=True)
    manufacturer_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = models.Aircraft
        fields = "__all__"
        read_only_fields = ["id"]

    def create(self, validated_data):
        return models.Aircraft.objects.create(**validated_data)


class Passenger(serializers.ModelSerializer):
    class Meta:
        model = models.Passenger
        fields = "__all__"
        read_only_fields = ["id"]


class Airport(serializers.ModelSerializer):
    class Meta:
        model = models.Airport
        fields = "__all__"
        read_only_fields = ["id"]


class Flight(serializers.ModelSerializer):
    crew_members = CrewMember(many=True, read_only=True)

    class Meta:
        model = models.Flight
        fields = "__all__"
        read_only_fields = ["id"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ["id"]


class Ticket(serializers.ModelSerializer):
    flight = Flight(read_only=True)
    flight_id = serializers.IntegerField(write_only=True)
    passenger = Passenger(read_only=True)
    passenger_id = serializers.IntegerField(write_only=True)

    user_id = serializers.IntegerField(write_only=True)
    buyer = UserSerializer(read_only=True)

    class Meta:
        model = models.Ticket
        fields = "__all__"
        read_only_fields = ["id"]
