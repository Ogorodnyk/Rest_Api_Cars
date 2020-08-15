from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cars_models.models import Car
from cars_models.api.serializers import CarSerializer


@api_view(["GET", "POST"])
def car_list_create_api_view(request):

    if request.method == "GET":
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def car_list_popular_api_view(request):
    if request.method == "GET":
        cars = Car.objects.order_by("-rate")
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
