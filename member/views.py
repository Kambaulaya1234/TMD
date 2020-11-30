from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from loan.models import Loan
from share.models import Share, WeekModel, YearModel


class IndexView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'members/member_list.html'
        members = Member.objects.filter(is_member=True, has_fine=False)
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
            object.is_member = True
            object.save()
            messages.success(self.request, 'Your member created successfully!')
            return redirect('member:index')
        else:
            messages.error(self.request, 'Validation error')
            return redirect('member:index')


class InactiveIndexView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'members/inactive_member_list.html'
        members = Member.objects.filter(is_member=True, has_fine=True)
        form = MemberForm()
        context = {
            'members': members,
            'form': form,
        }
        return render(request, template_name, context)


class StatusView(View):
    def post(self, request, *args, **kwargs):
        print(request.POST)
        week_ID = request.POST['week_id']
        year_ID = request.POST['year_id']
        member = Member.objects.filter(id=kwargs['id'])[0]
        _week = WeekModel.objects.filter(id=week_ID)[0]
        _year = YearModel.objects.filter(id=year_ID)[0]
        share = Share.objects.filter(member=member, week=_week, year=_year)[0]
        # ------------------------------------------------------
        member.has_fine = False
        share.fine = 20000
        share.hisa = 1
        share.jamii = 5000
        # ------------------------------------------------------
        member.save()
        share.save()
        # ------------------------------------------------------
        messages.success(request, 'member activated successfully!')
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


class PayLoanView(View, BaseObject):
    def post(self, *args, **kwargs):
        member = self.get_object(kwargs['id'])[0]
        amount = float(self.request.POST['amount'])
        deadline = self.request.POST['deadline']
        Loan.objects.create(member=member, amount=amount, deadline=deadline)
        messages.success(
            self.request, f'member {member.user} assigned loan  successfully!')
        return redirect('loan:index')
