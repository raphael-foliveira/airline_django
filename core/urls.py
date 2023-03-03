from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'core'

router = DefaultRouter()
router.register('aircrafts', views.Aircraft)
router.register('manufacturers', views.Manufacturer)
router.register('passengers', views.Passengers)
router.register('flights', views.Flight)
router.register('crew', views.CrewMember)
router.register('tickets', views.Ticket)


urlpatterns = router.urls
urlpatterns += [
    path('auth', obtain_auth_token)
]
