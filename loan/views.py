from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from .models import Loan
from django.core.paginator import Paginator


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
