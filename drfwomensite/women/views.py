from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women
from women.serializers import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request: Request):
        women_list = Women.objects.all().values()
        return Response(
            {"posts": list(women_list)}
        )

    def post(self, request: Request):
        new_post = Women.objects.create(
            title=request.data["title"],
            content=request.data["content"],
            category_id=request.data["category_id"]
        )
        return Response(
            {"post": model_to_dict(new_post)}
        )


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

