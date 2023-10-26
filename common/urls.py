from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PositionViewSet, RankViewSet, AcademicDegreeViewSet, \
    AcademicRankViewSet, AcademicRankUsage, AcademicDegreeUsage, ScientificPotential

router = DefaultRouter()
router.register(r'positions', PositionViewSet, basename='position')
router.register(r'ranks', RankViewSet, basename='rank')
router.register(r'academicdegrees', AcademicDegreeViewSet, basename='academicdegree')
router.register(r'academicranks', AcademicRankViewSet, basename='academicrank')

urlpatterns = [
    path('', include(router.urls)),
    path('academic_rank_usage/', AcademicRankUsage.as_view(), name='academic_rank_usage'),
    path('academic_degree_usage/', AcademicDegreeUsage.as_view(), name='academic_degree_usage'),
    path('scientific_potential/', ScientificPotential.as_view(), name='scientific_potential'),
]
