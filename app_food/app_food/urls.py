"""
URL configuration for app_food project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from corporate_food.views import main_page, about, contacts, create_order, get_order, \
    delete_order, all_dishes, create_dish, delete_dish

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name="main_page"),
    path('order', create_order, name="create_order"),
    path('about', about, name="about"),
    path('contacts', contacts, name="contacts"),
    path('order/new', create_order, name="new_order"),
    path('order/delete', delete_order, name="delete_order"),
    path('all_dishes', all_dishes, name="all_dishes"),
    path('delete_dish', delete_dish, name="delete_dish"),
]
