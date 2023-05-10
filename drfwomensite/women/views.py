from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from women.models import Women
from women.permissions import IsAdminOrReadOnly
from women.serializers import WomenSerializer


class WomenMixin:
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIList(WomenMixin, generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )


class WomenAPIUpdate(WomenMixin, generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )  # Auth only with token, not session


class WomenAPIDestroy(WomenMixin, generics.RetrieveDestroyAPIView):
    permission_classes = (IsAdminOrReadOnly, )
