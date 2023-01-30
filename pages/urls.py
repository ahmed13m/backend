from django.urls import path
from .views import homepage, mainpage

urlpatterns = [
    path('',homepage,name='home'),
    path('main/',mainpage.as_view(),name= 'main')
]