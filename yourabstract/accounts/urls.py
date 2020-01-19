from django.urls import path
from django.contrib.auth import views

from .views import registration

app_name = 'accounts'
urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
