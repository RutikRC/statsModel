# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StepsModelViewSet, ImageViewSet

router = DefaultRouter()
router.register(r'stepsModel', StepsModelViewSet, basename='StepsModels')
router.register(r'designs', ImageViewSet, basename='design')

urlpatterns = [
    path('', include(router.urls)),
]
