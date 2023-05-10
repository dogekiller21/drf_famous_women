from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women
from women.serializers import WomenSerializer


class WomenMixin:
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIList(WomenMixin, generics.ListCreateAPIView):
    ...


class WomenAPIUpdate(WomenMixin, generics.UpdateAPIView):
    ...


class WomenAPIDetailView(WomenMixin, generics.RetrieveUpdateDestroyAPIView):
    ...
