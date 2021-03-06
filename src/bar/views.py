from .models import ProductCategory, Product

from django.views.generic import ListView


class MenuView(ListView):
    model = ProductCategory
    template_name = "bar_menu.html"
    context_object_name = "categories"
