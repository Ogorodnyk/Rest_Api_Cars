from django.db import models

# Create your models here.

RATE = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
)


class CarRate(models.Model):
    rate = models.IntegerField(choices=RATE)

    def __str__(self):
        return F"{self.rate}"


class Car(models.Model):
    car_make = models.CharField(max_length=120)
    model_name = models.CharField(max_length=120)
    # rate = models.IntegerField(choices=RATE)
    rate = models.ManyToManyField(CarRate, related_name='care_rate')

    def __str__(self):
        return F"{self.car_make} {self.model_name} {self.rate}"


# class GiveRate(models.Model):
#     care_rate_id = models.ForeignKey(CarRate, on_delete=models.CASCADE)
#     car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
