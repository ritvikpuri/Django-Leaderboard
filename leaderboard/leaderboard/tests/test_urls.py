# from django.test import SimpleTestCase, TestCase
# from django.urls import resolve, reverse
# from leaderboard_api.views import LeaderboardAPIView, UserInfoAPI
# # from leaderboard_api.views import 

# class TestURL(TestCase):

#     def test_user_list_url(self):
#         url = reverse('leaderboard')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response['Content-Type'], 'application/json')

#     # def test_user_detail_api_url(self):
#     #     url = reverse('user-info', args=[1]) 
#     #     self.assertEqual(resolve(url).func.view_class, UserInfoAPI)