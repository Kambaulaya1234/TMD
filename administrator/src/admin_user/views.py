from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, Permission, User
from django.views import View
from accounts.models import Profile
from django.contrib import messages
from django.conf import settings
from .forms import *
from django.core.mail import BadHeaderError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# from mail_templated import EmailMessage


class Index(LoginRequiredMixin, View):
    template_name = 'users/user_active.html'

    def get(self, *args, **kwrgs):
        _users = User.objects.exclude(username='conic').order_by('id')
        users = [user for user in _users if user.profile.is_member == False]
        form = UserCreateForm()
        context = {
            'users': users,
            'form': form,
        }
        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        group_id = self.request.POST['groups'][0]
        context = {
            'username': self.request.POST['username'].lower(),
            'first_name': self.request.POST['first_name'],
            'last_name': self.request.POST['last_name'],
            'email': self.request.POST['email'],
            'password': 'atlais'
        }
        if not User.objects.filter(username=context['username']).exists():
            group = Group.objects.filter(id=group_id)
            user = User.objects.create_user(**context)
            user.groups.set(group)
            Profile.objects.create(user=user)

        # SUBJECT=f'Hello {user.username}'
        # BODY=f'WELCOME TO iCARE TECHNOLOGY,your password:icare'
        # FROM=settings.EMAIL_HOST_USER
        # TO_EMAIL=[user.email]
        # posted_by=self.request.user.username

            # if SUBJECT and BODY and FROM:
            #     try:
            #         email = EmailMessage('email/user.tpl', {'user': user,'group':group[0],'posted_by':posted_by}, FROM,
            #                to=TO_EMAIL)
            #         email.send()
            #         return redirect('administrator:user')
            #     except BadHeaderError:
            #         return redirect('administrator:user')
            # else:
            messages.success(
                self.request, f'user {user} created successfully!')
        else:
            _entered_name = context['username']
            messages.error(
                self.request, f'Sorry {self.request.user },name "{_entered_name}" already taken')
        return redirect('administrator:user')


@login_required
def update_user(request, id):
    context = {
        'username': request.POST['username'],
        'first_name': request.POST['first_name'],
        'last_name': request.POST['last_name'],
        'email': request.POST['email'],
    }
    group_id = request.POST['groups'][0]
    group = Group.objects.filter(id=group_id)
    user = User.objects.filter(id=id)
    user.update(**context)
    user[0].groups.set(group)
    return redirect('administrator:user')


@login_required
def remove_user(request, id):
    user = User.objects.filter(pk=id)
    user.delete()
    messages.success(request, 'selected Group deleted successfully!')
    return redirect('administrator:user')
