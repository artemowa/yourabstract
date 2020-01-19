from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Post


class PostListView(ListView):
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        context = Post.objects.filter(
            author__username=self.request.user.username
        )
        return context

