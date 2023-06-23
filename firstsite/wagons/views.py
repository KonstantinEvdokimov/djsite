from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """Возвращает экземпляр объекта HttpResponse.

    Этот экземпляр будет автоматически формировать нужный заголовок ответа,
    а содержимое HTML-страницы будет определяться указанной строкой.
    Параметр request – это ссылка на экземпляр класса HttpRequest,
    который содержит информацию о запросе, о сессии, о куках и так далее.
    То есть, через переменную request нам доступна вся возможная информация в рамках текущего запроса."""
    return HttpResponse("Страница приложения wagons.")

def categories(request):
    return HttpResponse(f"<h1>Статьи по категориям</h1>")