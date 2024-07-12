from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """Create user."""

    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)


class UserDestroyAPIView(DestroyAPIView):
    """Delete user."""

    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)
    queryset = User.objects.all()
