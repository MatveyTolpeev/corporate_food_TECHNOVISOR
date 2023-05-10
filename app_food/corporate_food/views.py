from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
from .other_functions import color_decorator
from .models import Order, OrderDish, Dish, Employee


@color_decorator
def main_page(request):
    if request.method == 'GET':
        data = {'name': 'corporate_food'}
        return render(request, 'index.html', data)


@color_decorator
def about(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT about_us_text FROM about_us")
        about_us_text = cursor.fetchall()
        data = {'text': about_us_text[0][0]}
        return render(request, 'about.html', data)


@color_decorator
def contacts(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM contacts")
        contacts = cursor.fetchall()
        refactor_contacts = [str(el[0]) + ':' + str(el[1]) for el in contacts]
        data = {'contacts': refactor_contacts}
        return render(request, 'contacts.html', data)


def get_order(request):
    pass


@color_decorator
def create_order(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        dishes = Dish.objects.all()
        employees_rendered = [el for el in employees]
        dishes_rendered = [el for el in dishes]
        print(f'{employees},{dishes}')
        data = {'employees': employees_rendered, 'dishes': dishes_rendered}
        return render(request, 'new_order.html', data)
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('price'):
            order = Order()
            service.name = request.POST.get('name')
            service.price = request.POST.get('price')
            if request.POST.get('description'):
                service.description = request.POST.get('description')
            service.save()
            out_green('[++] end services_new')
            return redirect('/services')
    else:
        out_green('[++] end services_new')
        return HttpResponse(request, '<h1>Метод запроса не поддерживается<h1>')


@color_decorator
def delete_order(request):
    pass


@color_decorator
def all_dishes(request):
    if request.method == 'GET':
        dishes_rendered = [el for el in Dish.objects.all()]
        data = {'dishes': dishes_rendered}
        return render(request, 'dishes.html', data)
    else:
        return HttpResponse(request, '<h3>Метод запроса не поддерживается</h3>')


@color_decorator
def create_dish(request):
    pass


@color_decorator
def delete_dish(request):
    pass
