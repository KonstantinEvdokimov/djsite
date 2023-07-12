from django import template
from django.http import Http404

from wagons.models import Wagons, Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('wagons/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}


@register.inclusion_tag('wagons/list_posts.html')
def show_posts(cat_id=0):
    if not cat_id:
        posts = Wagons.objects.all()
    else:
        posts = Wagons.objects.filter(cat=cat_id)

    return {"posts" : posts}