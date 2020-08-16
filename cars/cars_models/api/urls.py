from django.urls import path
from cars_models.api.views import CarListCreateAPIView, CarDetailAPIView
from cars_models.api.views import car_list_popular_api_view
# from cars_models.api.views import car_list_create_api_view, car_list_popular_api_view, car_detail_api_view

urlpatterns = [
    path("popular/", car_list_popular_api_view, name="popular-cars-list"),
    path("cars/<int:pk>", CarDetailAPIView.as_view(), name="cars-detail"),
    path("cars/", CarListCreateAPIView.as_view(), name="cars-list"),

]