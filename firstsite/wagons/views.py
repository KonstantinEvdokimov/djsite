from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddPostForm
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
    '''Добавление статьи через экземпляр класса Form.

    При повторном ее отображении, например, если данные были введены некорректно и нужно показать ошибки ввода,
    то форма должна сохранять ранее введенную пользователем информацию.
    Вначале проверяем, если пришел POST-запрос, значит, пользователем были отправлены данные.
    В этом случае наполняем форму принятыми значениями из объекта request.POST и, затем,
    делаем проверку на корректность заполнения полей (метод is_valid).'''
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Wagons.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')

    else:
        form = AddPostForm()
    return render(request, 'wagons/addpage.html', {'menu': menu, 'title': 'Добавление статьи', 'form': form})


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
