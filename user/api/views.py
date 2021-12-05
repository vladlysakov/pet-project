from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user.api.serializers import UserSerializer
from user.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = IsAuthenticated,
