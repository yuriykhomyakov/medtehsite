from django.urls import path
from . import views


app_name = 'bills'
urlpatterns = [
    path('', views.bill_list, name='bill_list'),
    path('bill/<int:pk>', views.bill_detail, name='bill_detail'),
    path('bill/<int:pk>/edit', views.bill_edit, name='bill_edit'),
    path('bill/new', views.bill_new, name='bill_new'),
]