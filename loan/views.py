from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from .models import Loan
from django.core.paginator import Paginator
from django.contrib import messages


class IndexView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'loans/loan_index.html'
        loans = Loan.objects.order_by('-created_at')
        paginator = Paginator(loans, 10)
        page = request.GET.get('page')
        filterItems = paginator.get_page(page)
        context = {
            'Loans': filterItems,
        }
        return render(request, template_name, context)


class BaseObject:
    def get_object(self, id):
        loan = Loan.objects.filter(id=id)
        return loan


class RemoveView(View, BaseObject):
    def get(self, *args, **kwargs):
        self.get_object(kwargs['id']).delete()
        messages.success(self.request, 'loan deleted successfully!')
        return redirect('loan:index')
