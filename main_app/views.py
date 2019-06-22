from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from .models import Item


# Create your views here.

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'

class ItemDelete(DeleteView):
    model = Item
    success_url = '/items'

def home(request):
    items = Item.objects.all()
    return render(request, 'home.html' , {'items': items})

def items_index(request):
  items = Item.objects.all()
  return render(request, 'items/index.html', { 'items': items })

def items_detail(request, item_id):
  item = Item.objects.get(id=item_id)
  return render(request, 'items/detail.html', { 'item': item })