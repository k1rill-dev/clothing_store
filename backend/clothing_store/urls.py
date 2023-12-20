from django.urls import path, include
from rest_framework import routers

from clothing_store.views import HatViewSet, FurCoatViewSet, GlovesViewSet, BagViewSet, PhotoFurCoatView, PhotoBagView, \
    PhotoGlovesView, PhotoHatView

router = routers.SimpleRouter()

router.register(r'hat', HatViewSet)
router.register(r'furcoat', FurCoatViewSet)
router.register(r'gloves', GlovesViewSet)
router.register(r'bag', BagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('photos-furcoat', PhotoFurCoatView.as_view(), name='photos_furcoat'),
    path('photos-bag', PhotoBagView.as_view(), name='photos_bag'),
    path('photos-gloves', PhotoGlovesView.as_view(), name='photos_gloves'),
    path('photos-hat', PhotoHatView.as_view(), name='photos_hat'),
]
