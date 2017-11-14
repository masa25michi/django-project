from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post


def post_list(request, category=None):

    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts':posts })