from django.urls import path
from . import views

app_name = 'orderprep'
urlpatterns = [
    path('orderpreparation/', views.OrderPrepView.as_view(), name='orderpreparation'),
    path('sales/', views.SalesView.as_view(), name='sales'),
    path('form/', views.FormView.as_view(), name='form'),
]