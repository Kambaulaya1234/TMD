from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

class Index(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        template_name='admin_dashboard.html'
        return render(request,template_name)
    
class NormalDashboard(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        template_name='normal_dashboard.html'
        return render(request,template_name)

