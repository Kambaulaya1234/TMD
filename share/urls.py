from django.urls import path
from .views import *

app_name = 'share'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('delete/<int:id>/', RemoveView.as_view(), name='delete'),
    # ===============================================================
    path('weeks/', ActiveWeekView.as_view(), name='weeks'),
    path('months/', ActiveMonthView.as_view(), name='months'),
    path('years/', ActiveYearView.as_view(), name='years'),
]
