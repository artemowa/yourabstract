from markdown import markdown

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField('Abstract title', max_length=50)
    slug = models.SlugField('Slug', max_length=100, unique=True)
    content = models.TextField('Abstract text')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
            related_name='posts_list', verbose_name='Author')
    publish = models.DateTimeField('Publish date', auto_now_add=True)

    class Meta:
        verbose_name = 'Abstract'
        verbose_name_plural = 'Abstracts'
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.content = markdown(self.content)
        super().save(*args, **kwargs)

