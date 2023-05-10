from django.core.exceptions import ObjectDoesNotExist
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
        serializer.save()  # For CRUD inside serializer
        return Response(
            {"post": serializer.data}
        )

    def put(self, request: Request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if pk is None:
            return Response(
                {"error": "Method PUT not allowed"},
                status=400
            )
        try:
            instance = Women.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(
                {"error": "Object not found"},
                status=400
            )
        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"post": serializer.data}
        )

    def delete(self, request: Request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if pk is None:
            return Response(
                {"error": "Method PUT not allowed"},
                status=400
            )
        try:
            instance: Women = Women.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(
                {"error": "Object not found"},
                status=400
            )
        instance.delete()
        return Response(
            {"deleted": f"Object with {pk=} was deleted"}
        )



# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

