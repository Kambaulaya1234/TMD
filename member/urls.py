from django.urls import path
from .views import *


app_name = 'member'
urlpatterns = [
    path('active-members/', IndexView.as_view(), name='index'),
    path('inactive/', InactiveIndexView.as_view(), name='inactive'),
    path('activate/<int:id>/', StatusView.as_view(), name='activate'),
    path('loan/<int:id>/', PayLoanView.as_view(), name='payloan'),
    path('create/', CreateMemberView.as_view(), name='create'),
    path('upload-member/',ImportMemberView.as_view(), name='upload'),
    path('profile/<int:id>',MemberProfileView.as_view(), name='profile'),
    path('fines/<int:id>',MemberFinesView.as_view(), name='fine'),
    path('delete/<int:id>/', RemoveView.as_view(), name='delete'),
    path('delete/all', RemoveAll.as_view(), name='delete_all'),
    path('edit/<int:id>/', EditMemberView.as_view(), name='edit'),
    path('download/', Download.as_view(), name='download'),

]
