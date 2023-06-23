from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def index(request):
    """Возвращает экземпляр объекта HttpResponse.

    Этот экземпляр будет автоматически формировать нужный заголовок ответа,
    а содержимое HTML-страницы будет определяться указанной строкой.
    Параметр request – это ссылка на экземпляр класса HttpRequest,
    который содержит информацию о запросе, о сессии, о куках и так далее.
    То есть, через переменную request нам доступна вся возможная информация в рамках текущего запроса."""
    return HttpResponse("Страница приложения wagons.")

def categories(request, typeid):
    return HttpResponse(f"<h1>Статьи по категориям</h1>{typeid}</p>")

def archive(request, year):
    if (int(year) > 2022):
        # raise Http404()
        # return redirect('/') # Временный редирект 302
        return redirect('home', permanent=True)# Постоянный редирект 301
    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Жаль! Страница не найдена</h1>')