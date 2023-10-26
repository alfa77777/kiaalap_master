from rest_framework import serializers

from common.models import AcademicDegree, AcademicRank
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    academic_degree = serializers.PrimaryKeyRelatedField(
        queryset=AcademicDegree.objects.all(),
        allow_null=True,
        required=False
    )
    academic_rank = serializers.PrimaryKeyRelatedField(
        queryset=AcademicRank.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Employee
        fields = '__all__'

