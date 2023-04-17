from django.http import HttpRequest
from rest_framework import viewsets, renderers, views
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from . import models, serializers


class Aircraft(viewsets.ModelViewSet):
    queryset = models.Aircraft.objects.all()
    serializer_class = serializers.Aircraft


class Manufacturer(viewsets.ModelViewSet):
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.Manufacturer


class CrewMember(viewsets.ModelViewSet):
    queryset = models.CrewMember.objects.all()
    serializer_class = serializers.CrewMember


class AirportView(viewsets.ModelViewSet):
    queryset = models.Airport.objects.all()
    serializer_class = serializers.Airport


class Passengers(viewsets.ModelViewSet):
    queryset = models.Passenger.objects.all()
    serializer_class = serializers.Passenger


class Flight(viewsets.ModelViewSet):
    queryset = models.Flight.objects.all()
    serializer_class = serializers.Flight


class Ticket(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = models.Ticket.objects.all()
    serializer_class = serializers.Ticket


class SomeView(views.APIView):
    def get(self, _: HttpRequest) -> Response:
        manufacturers = models.Manufacturer.objects.all()
        serializer = serializers.Manufacturer(manufacturers, many=True)
        return Response(
            {
                "message": "Hello, World!",
                "manufacturer": serializer.data,
            }
        )
