from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0
    }

    return render(request, 'wagons/index.html', context=context)


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)

    context = {
        'menu': menu,
        'title': category.name,
        'cat_selected': category.pk
    }

    return render(request, 'wagons/index.html', context=context)


def about(request):
    return render(request, 'wagons/about.html', {'title': 'О сайте'})


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_post(request, post_slug):
    post = get_object_or_404(Wagons, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'wagons/post.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Жаль! Страница не найдена</h1>')
