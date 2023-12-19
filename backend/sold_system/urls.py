from django.urls import path, include
from rest_framework import routers

from sold_system.views import HatSaleViewSet, FurCoatSaleViewSet, GlovesSaleViewSet, BagSaleViewSet

router = routers.SimpleRouter()
router.register(r'hat-sale', HatSaleViewSet)
router.register(r'furcoat-sale', FurCoatSaleViewSet)
router.register(r'gloves-sale', GlovesSaleViewSet)
router.register(r'bag-sale', BagSaleViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
