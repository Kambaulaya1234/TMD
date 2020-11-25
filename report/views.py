from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'report/report_index.html'
        context = {
            'balance': 'balance',
        }
        return render(request, template_name, context)
