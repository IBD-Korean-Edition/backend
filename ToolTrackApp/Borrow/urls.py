# borrow/urls.py
from django.urls import path
from .views import borrow_item

urlpatterns = [
    path('items', borrow_item, name='borrow_item'),
]
