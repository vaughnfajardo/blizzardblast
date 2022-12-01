from django.urls import path
from . import views

app_name = 'orderpreparation'
urlpatterns = [
    path('orderpreparation/', views.orderpreparation, name='orderpreparation'),
    #path('sales/', views.sales, name='sales'),
    #path('form/', views.form, name='form'),
]