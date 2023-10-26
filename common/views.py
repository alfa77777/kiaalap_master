from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from employees.models import Employee
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


class AcademicDegreeUsage(APIView):
    def get(self, request, format=None):
        academic_degree = AcademicDegree.objects.all()
        data = {}
        for degree in academic_degree:
            degree_name = degree.name
            employee_count = degree.employee_set.count()
            data[degree_name] = employee_count
        return Response(data)


class ScientificPotential(APIView):
    def get(self, request, format=None):
        employees = Employee.objects.all()
        academic_degree_count = 0
        only_dotsents_count = 0

        for employee in employees:
            if employee.academic_degree:
                academic_degree_count += 1
            elif str(employee.academic_rank).lower() == 'dotsent':
                only_dotsents_count += 1
        return Response((academic_degree_count+only_dotsents_count)*(100/218))

