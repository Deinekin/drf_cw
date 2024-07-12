from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@mail.com", password="1")
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            creator=self.user,
            place="Home",
            time="21:00:00",
            action="drink beer",
            is_pleasant=False,
            period=1,
            time_to_action="00:02:00",
            is_published=True,
        )

    def test_get_public_habits(self):
        url = reverse("habits:public_habits_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_create_habit(self):
        url = reverse("habits:habit_create")
        data = {
            "place": "home",
            "time": "22:00:00",
            "action": "drink water",
            "periodicity": 1,
            "time_to_action": 10,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_habit(self):
        url = reverse("habits:habit_detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), self.habit.place)

    def test_delete_habit(self):
        url = reverse("habits:habit_destroy", args=(self.habit.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_get_list_habits(self):
        url = reverse("habits:habit_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 4,
                    "place": "Home",
                    "time": "21:00:00",
                    "action": "drink beer",
                    "is_pleasant": False,
                    "period": "1",
                    "reward": None,
                    "time_to_action": "00:02:00",
                    "is_published": True,
                    "creator": 3,
                    "connection_habit": None,
                }
            ],
        }
        self.assertEqual(response.json(), data)
