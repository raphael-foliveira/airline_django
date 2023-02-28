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
    manufacturer = serializers.IntegerField()

    def validate_manufacturer(self, value):
        try:
            models.Manufacturer.objects.get(pk=value)
            return value
        except:
            raise serializers.ValidationError('manufacturer does not exist')

    def create(self):
        return models.Aircraft.objects.create(
            name=self.validated_data.get('name'),
            capacity=self.validated_data.get('capacity'),
            manufacturer_id=self.validated_data.get('manufacturer')
        )


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
