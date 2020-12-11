from django.urls import path
from .views import *

app_name = 'loan'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('complete', CompleteLoanListView.as_view(), name='complete'),
    path('delete/<int:id>', RemoveView.as_view(), name='delete'),
    path('paid/<int:id>', LoanProgressPaymentView.as_view(), name='paid'),
    path('show-payment/<int:id>', LoanShowView.as_view(), name='show'),
    path('delete-payment/<int:id>', RemovePaymentView.as_view(), name='delete_payment')

]
