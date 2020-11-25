from django.shortcuts import render,redirect
from .models import Member
from .forms import MemberForm
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from share.models import Share


class IndexView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'members/member_list.html'
        members = Member.objects.filter(is_member=True,has_fine=False)
        form = MemberForm()
        context = {
            'members': members,
            'form': form,
        }
        return render(request, template_name, context)

    def post(self, *args, **kwargs):
        form = MemberForm(self.request.POST or None)
        if form.is_valid():
            object = form.save(commit=False)
            object.is_member=True
            object.save()
            messages.success(self.request, 'Your member created successfully!')
            return redirect('member:index')
        else:
            messages.error(self.request, 'Validation error')
            return redirect('member:index')
        
class InactiveIndexView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'members/inactive_member_list.html'
        members = Member.objects.filter(is_member=True,has_fine=True)
        form = MemberForm()
        context = {
            'members': members,
            'form': form,
        }
        return render(request, template_name, context)
    
class StatusView(View):
    def post(self, request, *args, **kwargs):
        member = Member.objects.filter(id=kwargs['id'])[0]
        # member.has_fine=False
        # member.share.all()
        # Share.objects.filter(member=member,week=member.week)
        # member.save()
        return redirect('member:index')

class BaseObject:
    def get_object(self, id):
        member = Member.objects.filter(id=id)
        return member


class RemoveView(View, BaseObject):
    def get(self, *args, **kwargs):
        self.get_object(kwargs['id']).delete()
        messages.success(self.request, 'member deleted successfully!')
        return redirect('member:index')
