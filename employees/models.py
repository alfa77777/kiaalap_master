from django.db import models

from common.models import Position, Rank, AcademicDegree, AcademicRank
from departments.models import Department


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    academic_degree = models.ForeignKey(AcademicDegree, on_delete=models.CASCADE, null=True)
    academic_rank = models.ForeignKey(AcademicRank, on_delete=models.CASCADE, null=True)
    specialty = models.CharField(max_length=255)
    protected_time = models.DateField()


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

