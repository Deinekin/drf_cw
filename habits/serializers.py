from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import (ConnectedHabitOrRewardValidator,
                               ConnectionPleasantValidator,
                               NoRewardOrConnectionForPleasantValidator,
                               TimeDurationValidator)


class HabitSerializer(ModelSerializer):
    """Habit serializer class"""

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            ConnectedHabitOrRewardValidator(
                reward="reward", connection_habit="connection_habit"
            ),
            TimeDurationValidator(time="time_to_action"),
            ConnectionPleasantValidator(connect="", pleasant=""),
            NoRewardOrConnectionForPleasantValidator(
                pleasant="is_pleasant", connect="connection_habit", reward="reward"
            ),
        ]
