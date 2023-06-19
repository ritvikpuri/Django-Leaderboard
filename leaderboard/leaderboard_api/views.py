from django.shortcuts import render
from rest_framework import generics, status
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class LeaderboardAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-score')
    serializer_class = UserSerializer

class UserInfoAPI(APIView):
    def get(self, request, user_id):
        # user = get_object_or_404(User, id=user_id)
        user = User.objects.get(pk=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class IncreaseScoreAPIView(APIView):
    def patch(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        try:
            user = User.objects.get(pk=user_id)
            user.score += 1
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=404)

class DecreaseScoreAPIView(APIView):
    def patch(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        try:
            user = User.objects.get(pk=user_id)
            user.score -= 1
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=404)

class DeleteUserAPIView(APIView):
    def delete(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
            user.delete()
            return Response({'message': 'User deleted successfully.'}, status=204)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=404)