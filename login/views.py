from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView


class loginView(TemplateView):
    template_name = "login.html"


class dashboardView(TemplateView):
    template_name = "index.html"

# def dashboardView(request):
#     return render(request, 'dashboard.html')

