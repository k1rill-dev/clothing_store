from django.urls import path, include
from rest_framework import routers

from clothing_store.views import HatViewSet, FurCoatViewSet, GlovesViewSet, BagViewSet

router = routers.SimpleRouter()

router.register(r'hat', HatViewSet)
router.register(r'furcoat', FurCoatViewSet)
router.register(r'gloves', GlovesViewSet)
router.register(r'bag', BagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
