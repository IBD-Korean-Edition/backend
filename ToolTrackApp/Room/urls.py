from django.urls import path
from .views import room_detail
urlpatterns = [
    path('<int:id>/', room_detail, name='room_detail'),
]
