from rest_framework import serializers
from .models import Position, Rank, AcademicDegree, AcademicRank


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = '__all__'


class AcademicDegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicDegree
        fields = '__all__'


class AcademicRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicRank
        fields = '__all__'
