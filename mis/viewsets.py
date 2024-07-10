from rest_framework import viewsets
from mis.models import User, Course
from mis.serializers import UserSerializer, CourseSerializer


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CourseViewSets(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
