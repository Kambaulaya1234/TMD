from  django.urls import path
from . import views


app_name='member'
urlpatterns=[
    path('active/',views.IndexView.as_view(),name='index'),
    path('inactive/',views.InactiveIndexView.as_view(),name='inactive'),
    path('delete/<int:id>/', views.RemoveView.as_view(), name='delete')
    
]