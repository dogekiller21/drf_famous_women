from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women
from women.serializers import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request: Request):
        women_query_set = Women.objects.all()
        return Response(
            {"posts": WomenSerializer(women_query_set, many=True).data}
        )

    def post(self, request: Request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_post = Women.objects.create(
            title=request.data["title"],
            content=request.data["content"],
            category_id=request.data["category_id"]
        )
        return Response(
            {"post": WomenSerializer(new_post).data}
        )


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

