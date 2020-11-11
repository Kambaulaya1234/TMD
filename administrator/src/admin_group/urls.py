from django.urls import path,include
from .views import *


urlpatterns = [
    path('active-group/',Index.as_view(),name='group'),
    path('remove_group/<int:id>/',remove_group,name='remove_group'),
    path('update/<int:id>/',update_group,name='update_group'),
    path('grant/view/<int:id>/',Grant.as_view(),name='grant_access'),
    # path('grant/add_permissions/',PermissionGrant.as_view(),name='grant_permissions'),
]