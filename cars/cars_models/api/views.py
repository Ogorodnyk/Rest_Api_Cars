from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from cars_models.models import Car
from cars_models.api.serializers import CarSerializer, CarPopularSerializer
from django.db.models.functions import Length



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


@api_view(["GET", "PUT", "DELETE"])
def car_detail_api_view(request, pk):
    try:
        car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return Response({"error": {
            "code": 404,
            "message": "Car not found!"
        }}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CarSerializer(car)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def car_list_popular_api_view(request):
    if request.method == "GET":
        popular_cars = Car.objects.order_by('-rate')
        serializer = CarPopularSerializer(popular_cars, many=True)
        return Response(serializer.data)




class CarListCreateAPIView(APIView):

    def get(self, request, format=None):
        car = Car.objects.all()
        serializer = CarSerializer(car, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarDetailAPIView(APIView):

    def get_object(self, pk):
        car = get_object_or_404(Car, pk=pk)
        return car

    def get(self, request, pk):
        car = self.get_object(pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def put(self, request, pk):
        car = self.get_object(pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        car = self.get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

