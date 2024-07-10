from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "creator",
        "place",
        "time",
        "action",
        "is_pleasant",
        "connection_habit",
        "period",
        "reward",
        "time_to_action",
        "is_published",
    )
