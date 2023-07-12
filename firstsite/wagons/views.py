from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


class WagonsHome(ListView):
    model = Wagons
    template_name = 'wagons/index.html'
    context_object_name = 'posts'

    # extra_context = {'title': 'Главная страница'} # Подходит только для передачи статических данных (immutable data). Нельзя передать,например, список
    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Выполняет передачу в шаблон динамического и статического контекста.

        Внутри метода мы первым делом должны повторить работу этого метода базового класса.
        Здесь super() – это обращение к базовому классу и, далее, через точку, идет вызов аналогичного метода с передачей ему возможных именованных параметров из словаря kwargs.
        Сформированный базовый контекст мы сохраняем через переменную context.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        context['menu'] = menu
        return context

    def get_queryset(self):
        """
        Возвращает только опубликованные статьи.
        """
        return Wagons.objects.filter(is_published=True)


class WagonsCategory(ListView):
    model = Wagons
    template_name = 'wagons/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return Wagons.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


def about(request):
    return render(request, 'wagons/about.html', {'title': 'О сайте'})


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'wagons/addpage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['menu'] = menu
        return context


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


class ShowPost(DetailView):
    model = Wagons
    template_name = 'wagons/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Жаль! Страница не найдена</h1>')
