from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Rank(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AcademicDegree(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AcademicRank(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

