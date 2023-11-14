from rest_framework import serializers
from .models import ProjectInfo
from user.models import KYC


class ProjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInfo
        fields = "__all__"

    def _is_verified(self, obj):
        try:
            kyc = KYC.objects.get(user=obj.user)
            return kyc.status == "Approved"
        except KYC.DoesNotExist:
            return False
