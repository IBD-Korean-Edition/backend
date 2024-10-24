"""
URL configuration for ToolTrackBackend project.

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

from django.urls import path
from ToolTrackApp.Student.views import signup, login
from ToolTrackApp.Add.views import add_item
from django.contrib import admin
from django.urls import path, include
from ToolTrackApp.Remove.views import delete_item
from ToolTrackApp.Borrow.views import get_items_by_room, update_item

urlpatterns = [
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('admin/', admin.site.urls),
    path('borrow/', include('ToolTrackApp.Borrow.urls')),
    path('student/', include('ToolTrackApp.Student.urls')),
    path('room/', include('ToolTrackApp.Room.urls')),
    path('items/add', add_item),
    path('items/remove/<str:item_name>', delete_item),
    path('get_items_by_room',get_items_by_room),
    path('items/update/<str:item_name>', update_item),
]
