from django.shortcuts import render
from .models import ProjectInfo
from .serializers import ProjectInfoSerializer
from rest_framework import generics, permissions


class ProjectInfoCreate(generics.CreateAPIView):
    queryset = ProjectInfo.objects.all()
    serializer_class = ProjectInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectInfoUpdate(generics.RetrieveUpdateAPIView):
    queryset = ProjectInfo.objects.all()
    serializer_class = ProjectInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectInfoList(generics.ListAPIView):
    queryset = ProjectInfo.objects.all()
    serializer_class = ProjectInfoSerializer
    permission_classes = [permissions.AllowAny]


class UserProjectsList(generics.ListAPIView):
    serializer_class = ProjectInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ProjectInfo.objects.filter(user=self.request.user)
