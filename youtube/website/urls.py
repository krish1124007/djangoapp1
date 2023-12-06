from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('krish', admin.site.urls),
    path("" , views.index),
    path("login" , views.login1),
    path("codes" , views.codes1),
]
