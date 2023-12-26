from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Employee
from api.serializers import EmployeeSerializer



class EmployeeViewsetView(viewsets.ModelViewSet):
    serializer_class=EmployeeSerializer
    model=Employee
    queryset=Employee.objects.all()

    