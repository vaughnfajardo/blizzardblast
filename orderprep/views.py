from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views import View

# Create your views here.

def index(request):
    return HttpResponse('Hello! Order Prep View')

class OrderPrepView(View):
    def get(self, request):
        return HttpResponse('OrderPrepView')

class SalesView(View):
    def get(self, request):
        return HttpResponse('SalesView')

class FormView(View):
    def get(self, request):
        return HttpResponse('FormView')


