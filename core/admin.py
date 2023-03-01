from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Aircraft)
admin.site.register(models.Airport)
admin.site.register(models.Passenger)
admin.site.register(models.Flight)
admin.site.register(models.Ticket)
admin.site.register(models.CrewMember)
admin.site.register(models.CrewMember_Flight)
admin.site.register(models.Manufacturer)
