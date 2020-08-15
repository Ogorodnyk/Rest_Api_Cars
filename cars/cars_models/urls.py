from django.urls import path
from .views import car_list, car_detail # CarPopularDetailView, CarPopularListView


urlpatterns = [
    # path("", CarPopularListView.as_view(), name="car-list"),
    # path("cars/<int:pk>/", CarPopularDetailView.as_view(), name="car-detail"),
    path("cars/", car_list, name="car-detail"),
    path("cars/<int:pk>/", car_detail, name="car-detail"),

]