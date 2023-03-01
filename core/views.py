from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import models, serializers


class Aircraft(viewsets.ViewSet):
    def list(self, _: Request):
        aircrafts = models.Aircraft.objects.all()
        serializer = serializers.Aircraft(
            instance=aircrafts, many=True)
        return Response(serializer.data)

    def create(self, request: Request):
        serializer = serializers.AircraftCreate(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def retrieve(self, _: Request, pk=None):
        try:
            aircraft = models.Aircraft.objects.get(pk=pk)
            serializer = serializers.Aircraft(instance=aircraft)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status.HTTP_404_NOT_FOUND)

    def update(self, request: Request, pk=None):
        try:
            aircraft = models.Aircraft.objects.get(pk=pk)
            aircraft.capacity = request.data['capacity']
            aircraft.save()
            serializer = serializers.Aircraft(instance=aircraft)
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


class Manufacturer(viewsets.ViewSet):
    def list(self, _: Request):
        manufacturers = models.Manufacturer.objects.all()
        serializer = serializers.Manufacturer(
            instance=manufacturers, many=True)
        return Response(serializer.data)

    def retrieve(self, _: Request, pk=None):
        try:
            manufacturer = models.Manufacturer.objects.get(pk=pk)
            serializer = serializers.Manufacturer(
                instance=manufacturer)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status.HTTP_400_BAD_REQUEST)

    def create(self, request: Request):
        serializer = serializers.Manufacturer(
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


class CrewMember(viewsets.ViewSet):
    def list(self, _: Request):
        crew = models.CrewMember.objects.all()
        serializer = serializers.CrewMember(instance=crew, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def retrieve(self, _: Request, pk=None):
        try:
            crew_member = models.CrewMember.objects.get(pk=pk)
            serializer = serializers.CrewMember(instance=crew_member)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status.HTTP_400_BAD_REQUEST)

    def create(self, request: Request):
        serializer = serializers.CrewMember(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, _: Request, pk=None):
        try:
            crew_member = models.CrewMember.objects.get(pk=pk)
            crew_member.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status.HTTP_400_BAD_REQUEST)


class AirportView(viewsets.ModelViewSet):
    queryset = models.Airport.objects.all()
    serializer_class = serializers.Airport


class Passengers(viewsets.ModelViewSet):
    queryset = models.Passenger.objects.all()
    serializer_class = serializers.Passenger


class Flight(viewsets.ModelViewSet):
    queryset = models.Flight.objects.all()
    serializer_class = serializers.Flight


class Ticket(viewsets.ViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self):
        tickets = models.Ticket.objects.all()
        serializer = serializers.Ticket(instance=tickets, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def retrieve(self, request: Request, pk=None):
        try:
            ticket = models.Ticket.objects.get(pk=pk)
            serializer = serializers.Ticket(instance=ticket)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status.HTTP_400_BAD_REQUEST)

    def create(self, request: Request):
        try:
            request.data['buyer_id'] = request.user.id
            serializer = serializers.TicketCreate(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_201_CREATED)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk=None):
        try:
            ticket = models.Ticket.objects.get(pk=pk)
            ticket.delete()
            return Response(None, status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
