from rest_framework import serializers

from . import models


class CrewMember(serializers.ModelSerializer):
    class Meta:
        model = models.CrewMember
        fields = '__all__'
        read_only_fields = ['id']


class Manufacturer(serializers.ModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = '__all__'
        read_only_fields = ['id']


class Aircraft(serializers.ModelSerializer):
    manufacturer = Manufacturer()

    class Meta:
        model = models.Aircraft
        fields = '__all__'
        read_only_fields = ['id']


class AircraftCreate(serializers.Serializer):
    name = serializers.CharField()
    capacity = serializers.IntegerField()
    manufacturer_id = serializers.IntegerField()

    def validate_manufacturer(self, value):
        try:
            models.Manufacturer.objects.get(pk=value)
            return value
        except:
            raise serializers.ValidationError('manufacturer does not exist')

    def create(self, validated_data):
        return models.Aircraft.objects.create(**validated_data)


class Passenger(serializers.ModelSerializer):
    class Meta:
        model = models.Passenger
        fields = '__all__'
        read_only_fields = ['id']


class Airport(serializers.ModelSerializer):
    class Meta:
        model = models.Airport
        fields = '__all__'
        read_only_fields = ['id']


class Flight(serializers.ModelSerializer):
    crew_members = CrewMember(many=True)

    class Meta:
        model = models.Flight
        fields = '__all__'
        read_only_fields = ['id']


class Ticket(serializers.ModelSerializer):

    class Meta:
        model = models.Ticket
        fields = '__all__'
        read_only_fields = ['id']


class TicketCreate(serializers.Serializer):
    passenger_id = serializers.IntegerField()
    flight_id = serializers.IntegerField()
    price = serializers.IntegerField()
    number_of_bags = serializers.IntegerField()
    ticket_class = serializers.ChoiceField(choices=["FR", "EX", "EC"])
    buyer_id = serializers.IntegerField()

    def validate_passenger_id(self, value):
        try:
            models.Passenger.objects.get(pk=value)
            return value
        except:
            raise serializers.ValidationError('Passenger does not exist')

    def validate_flight(self, value):
        try:
            models.Flight.objects.get(pk=value)
            return value
        except:
            raise serializers.ValidationError('Flight does not exist')

    def validate_buyer(self, value):
        try:
            models.User.objects.get(pk=value)
            return value
        except:
            raise serializers.ValidationError('User does not exist')

    def create(self, validated_data):
        return models.Ticket.objects.create(**validated_data)
