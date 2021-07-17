from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


class DashboardView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'dashboard.html', {'object': self.request.user})