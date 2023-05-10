from typing import Any

from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from women.models import Women, Category
from women.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from women.serializers import WomenSerializer


class WomenMixin:
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIList(WomenMixin, generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )


class WomenAPIUpdate(WomenMixin, generics.RetrieveUpdateAPIView):
    permission_classes = (IsOwnerOrReadOnly, )


class WomenAPIDestroy(WomenMixin, generics.RetrieveDestroyAPIView):
    permission_classes = (IsAdminOrReadOnly, )


# class WomenViewSet(
#     mixins.CreateModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     mixins.ListModelMixin,
#     GenericViewSet
# ):
#     serializer_class = WomenSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#         if pk is None:
#             return Women.objects.all()
#         return Women.objects.filter(pk=pk)
#
#     @action(methods=["get"], detail=False, url_path="category")
#     def get_category(self, request: Request):
#         categories = Category.objects.all()
#         return Response(
#             {"categories": [category.name for category in categories]}
#         )
