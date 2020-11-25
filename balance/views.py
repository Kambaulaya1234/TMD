from django.shortcuts import render
from django.views import View
from .models import Balance


class IndexView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'balance/balance_index.html'
        if Balance.objects.exists():
            balance = Balance.objects.all()[0]
            context = {
                'balance': balance,
            }
            return render(request, template_name, context)
        return render(request, template_name)
