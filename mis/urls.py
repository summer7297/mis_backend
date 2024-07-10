from django.urls import path
from rest_framework.routers import DefaultRouter

from mis.viewsets import UserViewSets, CourseViewSets
from mis.views import login_view

router = DefaultRouter()
router.register('users', UserViewSets, basename='users')
router.register('courses', CourseViewSets, basename='courses')
urlpatterns = router.urls
urlpatterns += [
    path('api/login/', login_view, name='login'),
]