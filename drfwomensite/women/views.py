from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from women.models import Women
from women.permissions import IsAdminOrReadOnly
from women.serializers import WomenSerializer


class WomenAPIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 10000


class WomenMixin:
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIList(WomenMixin, generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = WomenAPIListPagination


class WomenAPIUpdate(WomenMixin, generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )  # Auth only with base token, not session


class WomenAPIDestroy(WomenMixin, generics.RetrieveDestroyAPIView):
    permission_classes = (IsAdminOrReadOnly, )
