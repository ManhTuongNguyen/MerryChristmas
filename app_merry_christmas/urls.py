from django.urls import path
from . import views


urlpatterns = [
    path('', views.merry_christmas, name='index'),
]
