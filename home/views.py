from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, *args, **kwargs):
        template_name = 'home/home.html'
        return render(self.request, template_name)
