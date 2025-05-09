"""
URL configuration for Caso_Medico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Caso_Medico.services.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('query/', query, name  = 'query'),
    path('personalized/', personalized, name='personalized'),
    path('data-graph/', get_graph_data, name='data-graph'),
    path('query-builder', query_builder_view, name='query-builder'),
    path('charge_csv/', charge_csv, name='charge_csv'),
]

