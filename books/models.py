from django.db import models

from departments.models import Department


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
