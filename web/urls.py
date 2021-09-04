from django.urls import path
from web.views import staff,  index, customer, activity

urlpatterns = [
    path('', index, name='index'),
    path('staff/', staff, name='staff'),
    path('customer/', customer, name='customer'),
    path('activity/', activity, name='activity'),
    path('leave/', activity, name='leave'),
]
