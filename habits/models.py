from datetime import timedelta

from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": "True", "null": "True"}


class Habit(models.Model):
    PERIOD_CHOICES = (
        ("1", "Ежедневная"),
        ("2", "Еженедельная"),
    )

    creator = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Создатель"
    )
    place = models.CharField(max_length=100, verbose_name="Место")
    time = models.TimeField(verbose_name="Время выполнения")
    action = models.CharField(max_length=255, verbose_name="Действие")
    is_pleasant = models.BooleanField(
        default=True, verbose_name="Признак приятной привычки"
    )
    connection_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, **NULLABLE, verbose_name="Связанная привычка"
    )
    period = models.IntegerField(
        default=1, choices=PERIOD_CHOICES, verbose_name="Период"
    )
    reward = models.CharField(max_length=100, **NULLABLE, verbose_name="Вознаграждение")
    time_to_action = models.DurationField(
        default=timedelta(minutes=2), verbose_name="Время на выполнение"
    )
    is_published = models.BooleanField(
        default=False, verbose_name="Признак публичности"
    )

    def __str__(self):
        return f"Я буду {self.action} в {self.time_to_action} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
