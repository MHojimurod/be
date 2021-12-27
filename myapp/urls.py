from django.urls import path
from .views import home,qabul
urlpatterns = [
    path('', home,name='home'),
    path('qabul/', qabul,name='qabul')
]