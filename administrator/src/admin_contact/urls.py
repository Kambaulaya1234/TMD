from django.urls import path
from .views import *
urlpatterns=[
    path('',Index.as_view(),name='contact' ),
    path('remove_contact/<int:id>/',remove_contact,name='remove_contact'),
    path('remove__all_contact/',remove__all_contact,name='remove__all_contact'),
]