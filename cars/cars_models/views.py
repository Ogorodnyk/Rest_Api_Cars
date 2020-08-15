from django.http import JsonResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Car


def car_list(request):
    cars = Car.objects.all()
    data = {"cars": list(cars.values())}
    response = JsonResponse(data)
    return response


def car_detail(request, pk):
    try:
        car = Car.objects.get(pk=pk)
        data = {"car": {
            "car_make": car.car_make,
            "car_model": car.model_name,
            "rate": car.rate,

        }}
        response = JsonResponse(data)
    except Car.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "car not found!"
            }},
            status=404)
    return response
# class CarPopularDetailView(DetailView):
#     model = Car
#     template_name = "cars/car.html"
#
#
# class CarPopularListView(ListView):
#     model = Car
#     template_name = "cars/car_list.html"
