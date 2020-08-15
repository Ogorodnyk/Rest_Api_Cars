from django.urls import path
from cars_models.api.views import car_list_create_api_view, car_list_popular_api_view

urlpatterns = [
    path("cars/", car_list_create_api_view, name="cars-list"),
    path("popular/", car_list_popular_api_view, name="popular-cars-list"),
]
