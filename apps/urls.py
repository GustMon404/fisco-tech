from django.urls import path, include
from rest_framework import routers

from apps.nfse.urls import router_nfse

router = routers.DefaultRouter()
router.registry.extend(router_nfse.registry)

urlpatterns = [
    path('', include(router.urls))
]
