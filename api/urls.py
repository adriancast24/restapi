from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'chofer', views.choferViweSet)
router.register(r'ubicacion', views.ubicacionViewSet)


urlpatterns = [
    path('', include(router.urls))
]
