from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)


class Dish(models.Model):
    name = models.CharField(max_length=100)
    composition = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=2)


class Order(models.Model):
    date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class OrderDish(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
