from django.urls import include, path
from rest_framework import routers

from user.api import views

router = routers.DefaultRouter()

router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
