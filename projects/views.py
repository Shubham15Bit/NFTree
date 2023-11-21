from django.shortcuts import render
from .models import ProjectInfo, PlantImage
from .serializers import ProjectInfoSerializer, PlantImageSerializer
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


class PlantImageCreate(generics.CreateAPIView):
    queryset = PlantImage.objects.all()
    serializer_class = PlantImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlantImageUpdate(generics.RetrieveUpdateAPIView):
    queryset = PlantImage.objects.all()
    serializer_class = PlantImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlantImageList(generics.ListAPIView):
    queryset = PlantImage.objects.all()
    serializer_class = PlantImageSerializer
    permission_classes = [permissions.AllowAny]


class ProjectPlantList(generics.ListAPIView):
    serializer_class = PlantImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs.get("project_id")
        if project_id:
            return PlantImage.objects.filter(project_id=project_id)
        else:
            return PlantImage.objects.all()
