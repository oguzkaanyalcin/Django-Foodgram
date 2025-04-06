from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<slug:recipe_title>", views.details, name="recipe_details"),
    path("category/<slug:recipe_title>", views.getFoodByCategory, name='tarif_by_category')
]