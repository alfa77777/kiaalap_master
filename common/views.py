from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Position, Rank, AcademicDegree, AcademicRank
from .serializers import PositionSerializer, RankSerializer, AcademicDegreeSerializer, AcademicRankSerializer

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class RankViewSet(viewsets.ModelViewSet):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer


class AcademicDegreeViewSet(viewsets.ModelViewSet):
    queryset = AcademicDegree.objects.all()
    serializer_class = AcademicDegreeSerializer


class AcademicRankViewSet(viewsets.ModelViewSet):
    queryset = AcademicRank.objects.all()
    serializer_class = AcademicRankSerializer


class AcademicRankUsage(APIView):
    def get(self, request, format=None):
        academic_ranks = AcademicRank.objects.all()
        data = {}
        for rank in academic_ranks:
            rank_name = rank.name
            employee_count = rank.employee_set.count()
            data[rank_name] = employee_count
        return Response(data)
