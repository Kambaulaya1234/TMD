from django.shortcuts import render, redirect
from django.views import View
from .models import Share, WeekModel, MonthModel, YearModel
from .forms import CreateShareForm
from django.contrib import messages
from django import forms
from django.core.paginator import Paginator
from datetime import datetime
from member.models import Member
from openpyxl import load_workbook


class IndexView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'share/share_index.html'
        if (MonthModel.objects.exists() and YearModel.objects.exists()):
            this_month = MonthModel.objects.order_by('-created_at')[0]
            this_year = YearModel.objects.order_by('-created_at')[0]
            weeks = WeekModel.objects.filter(
                month__lte=this_month, year__lte=this_year).order_by('-created_at')
            paginator = Paginator(weeks, 1)
            page = request.GET.get('page')
            filterItems = paginator.get_page(page)
            form = CreateShareForm()
            context = {
                'weeks': filterItems,
                'form': form,
            }
            return render(request, template_name, context)
        else:
            return render(request, template_name)

    def post(self, *args, **kwargs):
        form = CreateShareForm(self.request.POST or None)
        if form.is_valid():
            object = form.save(commit=False)
            if(object.hisa < 1 or object.jamii < 5000):
                object.member.has_fine = True
                object.member.save()
            object.save()
            messages.success(self.request, 'Your share created successfully!')
            return redirect('share:index')
        else:
            messages.error(self.request, '')
            return redirect('share:index')


class BaseObject:
    def get_object(self, id):
        share = Share.objects.filter(id=id)
        return share


class Update(View, BaseObject):
    def post(self, *args, **kwargs):
        share = self.get_object(kwargs['slug'])[0]
        form = CreateShareForm(self.request.POST or None, instance=share)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Your post updated successfully!')
            return redirect('share:index')
        else:
            messages.warning(self.request, 'Error Validation successfully!')
            return redirect('share:index')


class RemoveView(View, BaseObject):
    def get(self, *args, **kwargs):
        self.get_object(kwargs['id']).delete()
        messages.success(self.request, 'Share deleted successfully!')
        return redirect('share:index')


class ActiveWeekView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'share/share_week_index.html'
        weeks = WeekModel.objects.order_by('-created_at')
        paginator = Paginator(weeks, 10)
        page = request.GET.get('page')
        filterItems = paginator.get_page(page)
        form = CreateShareForm()
        context = {
            'weeks': filterItems,
            'form': form,
        }
        return render(request, template_name, context)


class ActiveMonthView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'share/share_month_index.html'
        weeks = MonthModel.objects.order_by('-created_at')
        paginator = Paginator(weeks, 10)
        page = request.GET.get('page')
        filterItems = paginator.get_page(page)
        form = CreateShareForm()
        context = {
            'months': filterItems,
            'form': form,
        }
        return render(request, template_name, context)


class ActiveYearView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'share/share_year_index.html'
        weeks = YearModel.objects.order_by('-created_at')
        paginator = Paginator(weeks, 10)
        page = request.GET.get('page')
        filterItems = paginator.get_page(page)
        form = CreateShareForm()
        context = {
            'years': filterItems,
            'form': form,
        }
        return render(request, template_name, context)


class HandleUploadedFileView(View):
    def post(self, *args, **kwargs):
        _share_file = self.request.FILES['file']
        workbook = load_workbook(_share_file.file)
        sheet = workbook.active
        for row in sheet.iter_rows(min_row=11, values_only=True):
            _created, _status = self.create_member_from_file(*row)
            if _status:
                messages.success(self.request, 'Share uploaded successfully!')
            else:
                messages.error(
                    self.request, f'member "{_created}" is not found in member list!')
        return redirect('share:index')

    def create_member_from_file(self, member_entry, year_entry, month_entry, week_entry, hisa, jamii):
        _member = Member.objects.filter(
            user__username__contains=member_entry).distinct()
        if _member.exists():
            _year, info = YearModel.objects.get_or_create(name=year_entry)
            _month, info = MonthModel.objects.get_or_create(
                name=month_entry, year__name=year_entry)
            _week, info = WeekModel.objects.get_or_create(
                name=week_entry, month=_month, year=_year)

            context = {
                'member': _member[0], 'week': _week, 'month': _month,
                'year': _year, 'hisa': hisa, 'jamii': jamii
            }

            _share, info = Share.objects.get_or_create(**context)
            if(_share.hisa < 1 or _share.jamii < 5000):
                _share.member.has_fine = True
                _share.member.save()
            return (member_entry, True)
        else:
            return (member_entry, False)
