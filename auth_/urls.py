from django.urls import path, include
from django.contrib.auth import views as views_
from . import views

urlpatterns = [
    path('login/', views_.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views_.LogoutView.as_view(), name='logout'),
    path('accounts/', include('allauth.urls')),
    path('', views.DashboardView.as_view(), name='dashboard'),
]
