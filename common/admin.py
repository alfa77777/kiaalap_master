from django.contrib import admin
from .models import Position, Rank, AcademicDegree, AcademicRank

admin.site.register(Position)
admin.site.register(Rank)
admin.site.register(AcademicDegree)
admin.site.register(AcademicRank)
