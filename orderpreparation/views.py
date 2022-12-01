from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views import View

from .models import Addon, Customer, Customization, Employee, Ingredient, Manager, Milkshake, Orders, Recipe, RecipeIngredient, Restock, Staff


# Create your views here.


def orderpreparation(request):
    order_list = Orders.objects.all()
    return render(request, 'orderpreparation.html', 
    {"order_list": order_list})

#def sales(request):


#class FormView(View):
#    def get(self, request):
#        return HttpResponse('FormView')


