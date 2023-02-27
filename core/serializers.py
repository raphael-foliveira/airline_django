from rest_framework import serializers

from . import models


class CrewMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CrewMember
        fields = '__all__'
        read_only_fields = ['id']


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = '__all__'
        read_only_fields = ['id']


class AircraftSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = models.Aircraft
        fields = '__all__'
        read_only_fields = ['id']


class AircraftCreateSerializer(serializers.Serializer):
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
            manufacturer_id=self.validated_data['manufacturer']
        )


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Passenger
        fields = '__all__'
        read_only_fields = ['id']


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Airport
        fields = '__all__'
        read_only_fields = ['id']


class FlightSerializer(serializers.ModelSerializer):
    crew_members = CrewMemberSerializer(many=True)

    class Meta:
        model = models.Flight
        fields = '__all__'
        read_only_fields = ['id']


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ticket
        fields = '__all__'
        read_only_fields = ['id']
