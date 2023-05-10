import datetime

from django.db import models


def get_deadline():
    return datetime.datetime.now() + datetime.timedelta(minutes=60)


class Position(models.Model):
    title = models.CharField(max_length=100)
    salary = models.FloatField(null=False, default=0)

    def __str__(self):
        return self.title


class Employee(models.Model):
    personal_bonus = models.FloatField(default=0)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING, null=True)
    photo = models.ImageField(upload_to='Employee_photos/' + str(name) +
                                        '_' + str(surname) + '_' + str(position), null=True)

    def __str__(self):
        return f'{self.name} {self.surname} {self.position}'


class Schedule(models.Model):
    time_start_work = models.TimeField(default=datetime.time(10, 0))
    time_end_work = models.TimeField(default=datetime.time(19, 0))
    day_work = models.DateField(default=0)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)


class Dish(models.Model):
    DIFFICULT = [
        ('easy', 'Простое'),
        ('medium', 'Среднее'),
        ('hard', 'Сложное'),
    ]

    name = models.CharField(max_length=100, unique=True)
    composition = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    difficult = models.CharField(choices=DIFFICULT, default='medium', max_length=100)
    photo = models.ImageField(upload_to='Dishes/'+str(name), null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(default=get_deadline())
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, null=True)


class OrderDish(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
