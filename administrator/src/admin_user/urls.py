from django.urls import path,include
from .views import *


urlpatterns = [
    path('active-user',Index.as_view(),name='user'),
    path('update_user/<int:id>/',update_user,name='update_user'),
    path('remove_user/<int:id>/',remove_user,name='remove_user'),
    # path('update/<int:id>/',update_group,name='update_user'),
    # path('grant/view/<int:id>/',Grant.as_view(),name='grant_access'),
]