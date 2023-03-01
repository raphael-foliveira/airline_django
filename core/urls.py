from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'core'

router = DefaultRouter()
router.register('aircrafts', views.Aircraft, basename='aircraft')
router.register('manufacturers', views.Manufacturer,
                basename='manufacturer')
router.register('passengers', views.Passengers, basename='passenger')
router.register('flights', views.Flight, basename='flight')
router.register('crew', views.CrewMember, basename='crew_member')
router.register('tickets', views.Ticket, basename='ticket')


urlpatterns = router.urls
urlpatterns += [
    path('auth', obtain_auth_token)
]
