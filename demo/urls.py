# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import *

router = DefaultRouter()
router.register(r'stepsModel', StepsModelViewSet, basename='StepsModels')
router.register(r'designs', ImageViewSet, basename='design')
router.register(r'model-users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
