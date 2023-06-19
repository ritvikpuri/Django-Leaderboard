"""leaderboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from leaderboard_api.views import LeaderboardAPIView, IncreaseScoreAPIView, DecreaseScoreAPIView, DeleteUserAPIView, UserInfoAPI
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/leaderboard/', LeaderboardAPIView.as_view(), name='leaderboard'),
    path('api/leaderboard/<int:user_id>/', UserInfoAPI.as_view(), name='user-info'),
    path('api/increase-score/', IncreaseScoreAPIView.as_view(), name='increase_score'),
    path('api/decrease-score/', DecreaseScoreAPIView.as_view(), name='decrease_score'),
    path('api/delete-user/<int:user_id>/', DeleteUserAPIView.as_view(), name='delete_user'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]
