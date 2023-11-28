from rest_framework import serializers
from .models import ProjectInfo, PlantImage, Transaction, ProjectReport
from user.models import KYC


class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = "__all__"

    # # Ensure that the image field is treated as a file upload
    # def create(self, validated_data):
    #     return PlantImage.objects.create(image=self.context['request'].data.get('image'), **validated_data)


class ProjectInfoSerializer(serializers.ModelSerializer):
    plant_images = PlantImageSerializer(many=True)

    class Meta:
        model = ProjectInfo
        fields = "__all__"

    def _is_verified(self, obj):
        try:
            kyc = KYC.objects.get(user=obj.user)
            return kyc.status == "Approved"
        except KYC.DoesNotExist:
            return False


class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class ProjectReportSerializer(serializers.ModelSerializer):
    total_plants = serializers.IntegerField(read_only=True)
    plant_types = serializers.CharField(read_only=True)


    class Meta:
        model = ProjectReport
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        project_info = instance.project

        if project_info:
            representation['total_plants'] = project_info.plants_planted
            representation['plant_types'] = project_info.plant_types

        return representation
