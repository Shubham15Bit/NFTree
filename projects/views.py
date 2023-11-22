from django.shortcuts import render
from .models import ProjectInfo, PlantImage
from .serializers import ProjectInfoSerializer, PlantImageSerializer
from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser


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


class ProjectInfoCreateList(generics.ListCreateAPIView):
    queryset = ProjectInfo.objects.all()
    serializer_class = ProjectInfoSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        print(self.request.data)
        plant_images_data = self.request.data.get("plant_images", None)
        project_instance = serializer.save(user=self.request.user)

        if plant_images_data:
            for plant_image_data in plant_images_data:
                PlantImage.objects.create(project=project_instance, **plant_image_data)

    def get_queryset(self):
        return ProjectInfo.objects.filter(user=self.request.user)
