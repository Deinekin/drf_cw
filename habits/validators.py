from datetime import timedelta

from rest_framework.serializers import ValidationError


class ConnectedHabitOrRewardValidator:
    """В модели не должно быть заполнено одновременно и поле вознаграждения,
    и поле связанной привычки. Можно заполнить только одно из двух полей."""

    def __init__(self, reward, connection_habit):
        self.reward = reward
        self.connection_habit = connection_habit

    def __call__(self, value):
        reward = dict(value).get(self.reward)
        connection_habit = dict(value).get(self.connection_habit)

        if reward and connection_habit:
            raise ValidationError(
                "Исключите одновременный выбор связанной привычки и указания вознаграждения."
            )


class TimeDurationValidator:
    """Время выполнения должно быть не больше 120 секунд."""

    def __init__(self, time):
        self.time_to_action = time

    def __call__(self, value):
        if value.get(self.time_to_action) > timedelta(seconds=120):
            raise ValidationError("Время выполнения должно быть не больше 120 секунд.")


class ConnectionPleasantValidator:
    """В связанные привычки могут попадать только привычки с признаком приятной привычки"""

    def __init__(self, connect, pleasant):
        self.is_pleasant = pleasant
        self.connection_habit = connect

    def __call__(self, value):
        if value.get(self.connection_habit) and not value.get(self.is_pleasant):
            raise ValidationError(
                "В связанные привычки могут попадать только привычки с признаком приятной привычки."
            )


class NoRewardOrConnectionForPleasantValidator:
    """У приятной привычки не может быть вознаграждения или связанной привычки."""

    def __init__(self, pleasant, connect, reward):
        self.reward = reward
        self.is_pleasant = pleasant
        self.connection_habit = connect

    def __call__(self, value):
        if value.get(self.is_pleasant) and (
            value.get(self.reward) or value.get(self.connection_habit)
        ):
            raise ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки."
            )
