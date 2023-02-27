from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response

from . import models, serializers


class AircraftView(viewsets.ViewSet):
    def list(self, _: Request):
        aircrafts = models.Aircraft.objects.all()
        serializer = serializers.AircraftSerializer(
            instance=aircrafts, many=True)
        return Response(serializer.data)

    def create(self, request: Request):
        serializer = serializers.AircraftCreateSerializer(
            data=request.data)
        if serializer.is_valid():
            serializer.create()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def retrieve(self, _: Request, pk=None):
        try:
            aircraft = models.Aircraft.objects.get(pk=pk)
            serializer = serializers.AircraftSerializer(instance=aircraft)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status.HTTP_404_NOT_FOUND)

    def update(self, request: Request, pk=None):
        try:
            aircraft = models.Aircraft.objects.get(pk=pk)
            aircraft.capacity = request.data['capacity']
            aircraft.save()
            serializer = serializers.AircraftSerializer(instance=aircraft)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status.HTTP_400_BAD_REQUEST)

    def delete(self, _: Request, pk=None):
        try:
            aircraft = models.Aircraft.objects.get(pk=pk)
            aircraft.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status.HTTP_400_BAD_REQUEST)


class ManufacturerView(viewsets.ViewSet):
    def list(self, _: Request):
        manufacturers = models.Manufacturer.objects.all()
        serializer = serializers.ManufacturerSerializer(
            instance=manufacturers, many=True)
        return Response(serializer.data)

    def retrieve(self, _: Request, pk=None):
        try:
            manufacturer = models.Manufacturer.objects.get(pk=pk)
            serializer = serializers.ManufacturerSerializer(
                instance=manufacturer)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status.HTTP_400_BAD_REQUEST)

    def create(self, request: Request):
        serializer = serializers.ManufacturerSerializer(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, _: Request, pk=None):
        try:
            models.Manufacturer.objects.get(pk=pk).delete()
            return Response(status=204)
        except Exception as e:
            return Response({'error': str(e)}, status.HTTP_204_NO_CONTENT)


class CrewMemberView(viewsets.ViewSet):
    def list(self, _: Request):
        crew = models.CrewMember.objects.all()
        serializer = serializers.CrewMemberSerializer(instance=crew, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def retrieve(self, _: Request, pk=None):
        try:
            crew_member = models.CrewMember.objects.get(pk=pk)
            serializer = serializers.CrewMemberSerializer(instance=crew_member)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status.HTTP_400_BAD_REQUEST)

    def create(self, request: Request):
        serializer = serializers.CrewMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk=None):
        try:
            crew_member = models.CrewMember.objects.get(pk=pk)
            crew_member.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status.HTTP_400_BAD_REQUEST)


class AirportView(viewsets.ModelViewSet):
    queryset = models.Airport.objects.all()
    serializer_class = serializers.AirportSerializer


class PassengersView(viewsets.ModelViewSet):
    queryset = models.Passenger.objects.all()
    serializer_class = serializers.PassengerSerializer


class FlightView(viewsets.ModelViewSet):
    queryset = models.Flight.objects.all()
    serializer_class = serializers.FlightSerializer


class TicketView(viewsets.ModelViewSet):
    queryset = models.Ticket.objects.all()
    serializer_class = serializers.TicketSerializer
