from django.urls import path
from .views import *

app_name = 'loan'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('delete/<int:id>', RemoveView.as_view(), name='delete')
    
]
