from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('users', views.user_info),
    path('results/<str:user_name>/<str:locations>/<str:languages>/<str:comments>', views.results),
    path('backhome', views.backhome),
]