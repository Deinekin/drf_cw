from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginations import CustomPagination
from habits.serializers import HabitSerializer
from users.permissions import IsCreator


class HabitListAPIView(ListAPIView):
    """List of habits."""

    serializer_class = HabitSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Habit.objects.all()
        return Habit.objects.filter(creator=user)


class HabitCreateAPIView(CreateAPIView):
    """Creating a habit."""

    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.creator = self.request.user
        habit.save()


class HabitRetrieveAPIView(RetrieveAPIView):
    """Retrieving a habit."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsCreator,
    )


class HabitUpdateAPIView(UpdateAPIView):
    """Updating a habit."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsCreator,
    )


class HabitDestroyAPIView(DestroyAPIView):
    """Destroying a habit."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsCreator,
    )


class HabitIsPublishedAPIView(ListAPIView):
    """Public habits list."""

    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_published=True)
    pagination_class = CustomPagination
