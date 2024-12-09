from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.mixins import UpdateModelMixin

from users.models import User
from users.serializers.user_serializers import UserSerializer, UserCreateSerializer, UserPartialUpdateSerializer


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = permissions.AllowAny,
    queryset = User.objects.all()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = permissions.AllowAny,
    queryset = User.objects.all()


class UserUpdateAPIView(UpdateAPIView, UpdateModelMixin):
    permission_classes = permissions.AllowAny,
    serializer_class = UserPartialUpdateSerializer
    queryset = User.objects.all()

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class UserRetrieveAPIView(RetrieveAPIView):
    permission_classes = permissions.AllowAny,
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(DestroyAPIView):
    permission_classes = permissions.AllowAny,
    queryset = User.objects.all()
