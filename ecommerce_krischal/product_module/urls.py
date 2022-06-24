from django.urls import path
from .views import index, index1
urlpatterns = [
    path('', index),
    path('index1', index1),

]
