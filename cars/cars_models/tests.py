from django.test import TestCase

# Create your tests here.
import pytest

from .models import Car, GiveRate


@pytest.mark.django_db
def test_post_car(client, set_up):
    car_before = Car.objects.count()
    new_car = {
        "car_make": "Bmw",
        "model_name": "x6",
    }
    response = client.post("/movies/", new_car, format='json')
    assert response.status_code == 201
    assert Car.objects.count() == car_before + 1
    for key, value in new_car.items():
        assert key in response.data
        if isinstance(value, list):
            # Compare contents regardless of their order
            assert len(response.data[key]) == len(value)
        else:
            assert response.data[key] == value


@pytest.mark.django_db
def test_get_car_list(client, set_up):
    response = client.get("/cars/", {}, format='json')

    assert response.status_code == 200
    assert Car.objects.count() == len(response.data)


@pytest.mark.django_db
def test_get_car_detail(client, set_up):
    response = client.get("/cars/1/", {}, format='json')

    assert response.status_code == 200
    for field in ('id', 'car_make', 'model_name', 'average_rates'):
        assert field in response.data


@pytest.mark.django_db
def test_get_car_popular(client, set_up):
    response = client.get("/popular/", {}, format='json')

    assert response.status_code == 200
    for field in ('id', 'car_make', 'model_name', 'rate'):
        assert field in response.data
