from unicodedata import category, name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Inventory
from django.urls import reverse

def welcome(request):
    return HttpResponse("Добро пожаловать в наш магазин!")

def form(request):
    return render(request, 'form.html')

def inventory_view(request):
    inventories = Inventory.objects.all()
    return render(request, 'inventories_list.html', {'inventories': inventories})

def filter_inventories(request, id):
    inventories = Inventory.objects.filter(category__id = id)
    return render(request, 'inventories_list.html', {'inventories': inventories})

def detail_view(request, id):
    single_invent = Inventory.objects.get(id=id)
    return render(request, 'single_invent.html', {'single_invent': single_invent})

def delete_view(request, id):
    delete_invent = Inventory.objects.get(id=id)
    delete_invent.delete()
    return HttpResponse("This inventory has been deleted")

def create_view(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, 'create_invent.html', {'categories': categories}) 
    
    if request.method == "POST":
        name = request.POST.get("name")
        inventory_number = request.POST.get("inventory_number")
        category_id = request.POST.get("category")
        initial_cost = request.POST.get("initial_cost")
        residual_value = request.POST.get("residual_value")
        
        category=Category.objects.get(id=category_id)

        new_invent = Inventory(
            name=name, 
            inventory_number=inventory_number,
            initial_cost=initial_cost,
            residual_value=residual_value,
            category=category, 
            )
        new_invent.save()

        return redirect(reverse("all_inventories"))

def update_view(request, id):
    single_invent = Inventory.objects.get(id=id)
    if request.method == "GET":
        categories = Category.objects.all()
        context = {
            'categories': categories,
            'single_invent': single_invent
        }
        return render(request, 'update_invent.html', context) 
    
    if request.method == "POST":
        name = request.POST.get("name")
        inventory_number = request.POST.get("inventory_number")
        category_id = request.POST.get("category")
        initial_cost = request.POST.get("initial_cost")
        residual_value = request.POST.get("residual_value")
        
        category=Category.objects.get(id=category_id)

        single_invent.name = name
        single_invent.inventory_number = inventory_number
        single_invent.category = category
        single_invent.initial_cost = initial_cost
        single_invent.residual_value = residual_value
        single_invent.save()

        return redirect(reverse("all_inventories"))


def detail_view_category(request, id):
    single_cat = Category.objects.get(id=id)
    return render(request, 'single_cat.html', {'single_cat': single_cat})


def delete_view_category(request, id):
    delete_cat = Category.objects.get(id=id)
    delete_cat.delete()
    return HttpResponse("This category has been deleted")

def create_view_category(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, 'create_categ.html', {'categories': categories}) 
    
    if request.method == "POST":
        name = request.POST.get("name")
        first_invent_numbers = request.POST.get("first_invent_numbers")
        balance_group = request.POST.get("balance_group")
        
        new_category = Category(
            name=name, 
            first_invent_numbers=first_invent_numbers,
            balance_group=balance_group,
        )
        
        new_category.save()

        return redirect(reverse("all_inventories"))