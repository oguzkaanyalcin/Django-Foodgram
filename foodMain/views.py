from datetime import date
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Food, Categories
from django.core.paginator import Paginator

def index(request):
    recipe = Food.objects.all().order_by("-date")
    kategoriler = Categories.objects.all()
    paginator = Paginator(recipe, 4)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)
    return render(request, "foods/index.html", {
        "page_obj": page_obj,
        "categories": kategoriler
    })

def details(request, recipe_title):
    try:
        recipe = Food.objects.get(slug=recipe_title)
        kategoriler = Categories.objects.all()
    except:
        raise Http404()
    context = {
        'recipe': recipe,
        'categories': kategoriler
    }
    return render(request, 'foods/details.html', context)

def getFoodByCategory(request, recipe_title):
    recipes = Food.objects.filter(categories__slug = recipe_title).order_by("-date")
    category = Categories.objects.all()
    paginator = Paginator(recipes, 4)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)
    return render(request, "foods/index.html", {
        "recipe": recipes,
        "page_obj": page_obj,
        "categories": category,
        "selectCategory": recipe_title
    })