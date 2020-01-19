from django.shortcuts import render, redirect
from django.urls import reverse


def redirect_user(request):
    if request.user.is_authenticated:
        return redirect(reverse('posts:post_list'))
    else:
        return redirect(reverse('accounts:login'))
