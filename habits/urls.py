from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView, HabitDestroyAPIView,
                          HabitIsPublishedAPIView, HabitListAPIView,
                          HabitRetrieveAPIView, HabitUpdateAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path("", HabitListAPIView.as_view(), name="habit_list"),
    path("create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("detail/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_detail"),
    path("update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit_destroy"),
    path(
        "public_habits/", HabitIsPublishedAPIView.as_view(), name="public_habits_list"
    ),
]
