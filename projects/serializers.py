from rest_framework import serializers
from .models import ProjectInfo, PlantImage
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
