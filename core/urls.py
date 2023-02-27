from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'core'

router = DefaultRouter()
router.register('aircrafts', views.AircraftView, basename='aircraft')
router.register('manufacturers', views.ManufacturerView,
                basename='manufacturer')
router.register('passengers', views.PassengersView, basename='passenger')
router.register('flights', views.FlightView, basename='flight')
router.register('crew', views.CrewMemberView, basename='crew_member')


urlpatterns = router.urls
