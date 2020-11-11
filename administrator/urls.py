
from django.urls import path,include
from .views import *

app_name='administrator'

TEAM_URLS = [
    path('group/',include('administrator.src.admin_group.urls')),
    path('user/',include('administrator.src.admin_user.urls')),
    path('contact/',include('administrator.src.admin_contact.urls')),
]

urlpatterns = [
 # =======================init site======================================
    path('',Index.as_view(),name='index'),

# =======================admin 2 site======================================
    path('',include(TEAM_URLS)),
]
