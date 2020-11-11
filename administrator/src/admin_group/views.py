from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import Group,Permission,User
from django.contrib import messages
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.template.loader import get_template
from django.template import Context
import datetime



class Index(LoginRequiredMixin,View):
    login_url='login'
    template_name='groups/group_index.html'

    def get(self,*args,**kwargs):
      groups=Group.objects.order_by('id')
      form=GroupCreateForm()

      context={
          'groups':groups,
          'form':form,
      }
      return render(self.request,self.template_name,context)


    def post(self,*args,**kwargs):
        form=GroupCreateForm(self.request.POST)
        if form.is_valid():
            instance=form.instance
            form.save()
            return redirect('administrator:grant_access',instance.id )


def remove_group(request,id):
    group=Group.objects.filter(pk=id)
    if 'administrator'  in group or 'client' in group:
        messages.error(request,'you can\'t delete this group ')
        return redirect('administrator:group')
    else:
        keep=group[0]
        group.delete()
        messages.success(request,f'selected {keep.name} Group deleted successfully!')
        return redirect('administrator:group')

def update_group(request,id):
    group=Group.objects.filter(pk=id)
    form=GroupCreateForm(request.POST, instance=group[0])
    if form.is_valid():
        instance=form.instance
        form.save()
        messages.success(request,f'{instance.name.capitalize()} Group updated successfully!')
        return redirect('administrator:group')

class Grant(View):
    template_name='groups/grant.html'
    def get(self,*args,**kwargs):
        id=kwargs['id']
        group=Group.objects.filter(pk=id)[0]
        # permissions=Permission.objects.order_by('content_type')
        permissions=Permission.objects.all()
        context={
        'group':group,
        'permissions':permissions,
        }
        return render(self.request,self.template_name,context)



    def post(self,request,id,*args,**kwargs):
        perms=Permission.objects.all()
        group=Group.objects.filter(id=id)[0]
        request_permited=[]
        permited=[]
        for req in request.POST:
            request_permited.append(req)

        for onlypermited in request_permited[1:]:
            permission=Permission.objects.filter(codename=onlypermited)[0]
            permited.append(permission)
            
        group.permissions.set(permited)
        numb=group.permissions.all().count()

        # temp=get_template('email/user.html')
        # datadict={'user': request.user,'group':group.name  }
        # rendered=temp.render(datadict)
        # mail.send(
        # 'cbunih@gmail.com', # List of email addresses also accepted
        # settings.EMAIL_HOST_USER,
        # subject=f'new Group {group.name}',
        # message=f'[{group.name.upper() } GROUP CREATED INFO ]',
        # html_message=rendered,
        #           )

        messages.success(request,f'{group.name.capitalize()} Group created and {numb} Permissions applied successfully!')
        return redirect('administrator:group')

                # else:
                #     group.permissions.exclude(codename=perm.codename).delete()
                #     messages.success(self.request,'Permissiond applied successfully!')
                #     return redirect('administrator:group')

