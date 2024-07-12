from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_habit_telegram():
    habits = Habit.objects.all()
    for habit in habits:
        if habit.creator.chat_id:
            message = f"Выполни {habit.action} в {habit.time_to_action}"
            send_telegram_message(habit.creator.chat_id, message)
