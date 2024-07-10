from django.urls import path
from rest_framework.routers import DefaultRouter

from mis.viewsets import UserViewSets, CourseViewSets

router = DefaultRouter()
router.register('users', UserViewSets, basename='users')
router.register('courses', CourseViewSets, basename='courses')
urlpatterns = router.urls
