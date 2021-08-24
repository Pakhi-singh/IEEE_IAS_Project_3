from django.shortcuts import render
from .models import Item

# Create your views here.

def home(request):
    context = {}
    return render(request, 'home.html', context)

def item_list(request):
    context = {
        "items": Item.objects.all()
    }
    return render(request, "products/item_list.html", context)
