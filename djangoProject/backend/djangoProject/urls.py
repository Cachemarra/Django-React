"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# Imports
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend.todo import views


# Router
# This allow us to perform CRUD operations and the following queries:
# /todos/ -> list of al To do items. CREATE and READ operations.
# /todos/id -> returns a single To do item using the id. UPDATE and DELETE ops.
router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')


# URLS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)) # URL for the API.
]
