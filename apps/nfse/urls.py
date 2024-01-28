from django.urls import path, include
from rest_framework import routers

from .views import NfseModelViewSet

router_nfse = routers.DefaultRouter()
router_nfse.register('nfse', NfseModelViewSet)

# urlpatterns = [
#     path('', include(router_nfse.urls))
# ]

