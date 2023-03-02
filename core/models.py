from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)


class Aircraft(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(
        to=Manufacturer, on_delete=models.CASCADE, related_name="aircrafts")
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.manufacturer.name} {self.name}'


class CrewMember(models.Model):
    class CrewMemberRoles(models.TextChoices):
        PILOT = 'PL', _('Pilot')
        COPILOT = 'CP', _('Co-pilot')
        STEWARD = 'ST', _('Steward')

    role = models.CharField(choices=CrewMemberRoles.choices,
                            max_length=2, default=CrewMemberRoles.STEWARD)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.role})'


class Airport(models.Model):
    iata = models.CharField(max_length=3)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.city} ({self.iata})'


class Flight(models.Model):
    number = models.CharField(max_length=10)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField(null=True)
    aircraft = models.ForeignKey(
        to=Aircraft, on_delete=models.CASCADE, related_name="flights")
    departure_airport = models.ForeignKey(
        to=Airport, related_name='flights_depart', on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey(
        to=Airport, related_name='flights_arrive', on_delete=models.CASCADE)

    def __str__(self):
        return self.number + ": " + self.departure_airport.iata + " - " + self.arrival_airport.iata


class CrewMember_Flight(models.Model):
    crew_member = models.ForeignKey(
        to=CrewMember, related_name='flights', on_delete=models.CASCADE)
    flight = models.ForeignKey(
        to=Flight, related_name='crew', on_delete=models.CASCADE)


class Passenger(models.Model):
    first_names = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    payment_method = models.CharField(max_length=20)


class Ticket(models.Model):
    class TicketClass(models.TextChoices):
        FIRST = 'FR', _('First Class')
        EXECUTIVE = 'EX', _('Executive Class')
        ECONOMY = 'EC', _('Economy Class')

    passenger = models.ForeignKey(
        to=Passenger, on_delete=models.CASCADE, related_name='tickets')
    flight = models.ForeignKey(
        to=Flight, on_delete=models.CASCADE, related_name='tickets')
    price = models.IntegerField()
    number_of_bags = models.IntegerField()
    ticket_class = models.CharField(
        choices=TicketClass.choices, max_length=2, default=TicketClass.ECONOMY)
    buyer = models.ForeignKey(to=User, on_delete=models.PROTECT)
