from django.test import TestCase
from django.urls import reverse
from .models import User
from rest_framework.test import APIClient
from rest_framework import status

class UserCreationTestCase(TestCase):
    def test_create_user_valid_credentials(self):
        client = APIClient()

        # valid user data
        user_data = {
            'name': 'ritvik',
            'age': 10,
        }

        response = client.post('/api/leaderboard/', user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
    
    # split into 2 
    def test_create_user_invalid_credentials(self):
        client = APIClient()

        # invalid user data
        user_data = {
            'name': '100',
            'age': -10,
        }

        response = client.post('/api/leaderboard/', user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

class UserOrderingTestCase(TestCase):
    
    def test_users_ordered_by_scores(self):

        User.objects.create(name='alpha', score=100, age=20)
        User.objects.create(name='beta', score=200, age=40)
        User.objects.create(name='gamma', score=150, age=60)

        client = APIClient()

        response = client.get('/api/leaderboard/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        users = response.data
        scores = [user['score'] for user in users]
        self.assertEqual(scores, [200, 150, 100])

class DeleteUserAPITestCase(TestCase):

    def test_delete_user_api(self):
        self.user = User.objects.create(name='alpha', score=8, age=25)
        client = APIClient()

        response = client.delete(f'/api/delete-user/{self.user.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(User.objects.filter(id=self.user.id).exists())

