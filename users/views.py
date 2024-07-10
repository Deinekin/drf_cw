from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

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


class UserDestroyAPIView(DestroyAPIView):
    """Delete user."""

    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
