from django.http import HttpResponse
from django.shortcuts import render
from foodMain.models import Food, Categories
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

def category(request):
    recipe = Food.objects.all().order_by("-date")
    kategoriler = Categories.objects.all()
    paginator = Paginator(kategoriler, 10)
    category = request.GET.get('category', 1)
    category_obj = paginator.page(category)
    return render(request, "foods/category.html", {
        "category_obj": category_obj,
        "recipe": recipe
    })