from django.urls import path

from . import views

app_name = 'redirect'
urlpatterns = [
    path('', views.redirect_user, name='redirect_user'),
]
