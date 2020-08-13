from django.db import models

# Create your models here.

RATE = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
)


class Car(models.Model):
    car_make = models.CharField(max_length=120)
    model_name = models.CharField(max_length=120)
    rate = models.FloatField(choices=RATE)

    def __str__(self):
        return self.name
