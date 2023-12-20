from django.urls import path, include
from rest_framework import routers

from sold_system.views import HatSaleViewSet, FurCoatSaleViewSet, GlovesSaleViewSet, BagSaleViewSet, BuySameProductsView

router = routers.SimpleRouter()
router.register(r'hat-sale', HatSaleViewSet)
router.register(r'furcoat-sale', FurCoatSaleViewSet)
router.register(r'gloves-sale', GlovesSaleViewSet)
router.register(r'bag-sale', BagSaleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('buy', BuySameProductsView.as_view(), name="buy")
]
