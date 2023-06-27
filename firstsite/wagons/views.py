from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
posts = Wagons.objects.all()

def index(request):
    return render(request, 'wagons/index.html', {'posts': posts,'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'wagons/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, typeid):
    return HttpResponse(f"<h1>Статьи по категориям</h1>{typeid}</p>")


def archive(request, year):
    if (int(year) > 2022):
        # raise Http404()
        # return redirect('/') # Временный редирект 302
        return redirect('home', permanent=True)  # Постоянный редирект 301
    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Жаль! Страница не найдена</h1>')
