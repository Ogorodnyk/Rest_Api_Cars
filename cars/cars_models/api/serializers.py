from rest_framework import serializers
from cars_models.models import Car, CarRate
from django.db.models import Sum, Avg, Max, Min, Count, F, Q
from django.db.models import OuterRef


# class CarSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     car_make = serializers.CharField()
#     model_name = serializers.CharField()
#     rate = serializers.IntegerField()
#
#     def create(self, validated_data):
#         print(validated_data)
#         return Car.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.car_make = validated_data.get('car_make', instance.car_make)
#         instance.model_name = validated_data.get('model_name', instance.model_name)
#         instance.rate = validated_data.get('rate', instance.rate)
#         instance.save()
#         return instance

class CarSerializer(serializers.ModelSerializer):
    average_rates = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ('id', 'car_make', 'model_name', 'average_rates')

    def get_average_rates(self, obj):
        average_rates = Car.objects.all().aggregate(average_rates=Avg('rate'))
        return average_rates["average_rates"]


class CarPopularSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('id', 'car_make', 'model_name', 'rate')


class CarRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarRate
        fields = ('rate')
