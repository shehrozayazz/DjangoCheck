from django.urls import path
from . import views

urlpatterns=[
    path('',views.CBview.as_view()),
    path('add/',views.Result.as_view())



]