from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.db.models import Q

def get_items(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    items = Item.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(id__icontains=q))
    context = {'items': items}
    return render(request, 'list.html', context)

def add_item(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/app/list')

    context = {'form': form}
    return render(request, 'itemform.html', context)

def edit_item(request, pk):
    item = Item.objects.get(id=pk)
    form = ItemForm(instance=item)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect('list')

    context = {'form' : form}
    return render(request, 'itemform.html', context)

def delete_item(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'GET':
        item.delete()
        return redirect('list')
    context = {}
    return render(request, 'list.html', context)

def sort_by_id(request):
    Item._meta.ordering = ["id", "name"]
    return redirect('list')

def sort_by_name(request):
    Item._meta.ordering = ["name", "id"]
    return redirect('list')