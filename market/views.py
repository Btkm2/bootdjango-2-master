from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from .models import Products
from .forms import ProductsForm
from django.views.generic import DetailView, UpdateView
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

from market import forms

# Create your views here.

def course_info(request):
    return render(request, 'shop/course_info.html', {})

def dev_contacts(request):
    address = 'улица Манаса 8, Алматы 050000'
    dev_list = ({'name': 'Assel Orynbassar', 'phone': '+7 (777) 777-77-77', 'email': '28308@iitu.edu.kz', 'hours': '08:00 AM - 6:00 PM'},
                {'name': 'Muratbekuly Beket', 'phone': '+7 (777) 777-77-88', 'email': '27214@iitu.edu.kz', 'hours': '08:00 AM - 6:00 PM'})
    return render(request, 'shop/dev_contacts.html', context={'devs': dev_list, 'address': address})
    #return render(request, 'shop/dev_contacts.html', {})

def team_members(request):
    return render(request, 'shop/team_members.html', {})

def profile_page(request):
    return render(request, 'shop/profile.html', {})

def main_page(request):
    catalogue = ({})
    prods = Products.objects.all()
    return render(request, 'shop/index.html', {'products':prods})

def catalogue_page(request):
    catalogue = ({})
    prods = Products.objects.all()
    return render(request, 'shop/catalogue.html', {'products':prods})

def login_page(request):
    return render(request, 'shop/login.html', {})

def reg_page(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = RegisterForm()

    return render(request, 'shop/register.html', {"form":form})


class ProductsDetailed(DetailView):
    model = Products
    template_name = 'shop/detailed.html'
    context_object_name = 'product'

class ProductsUpdate(UpdateView):
    model = Products
    template_name = 'shop/create.html'
    # fields = ['title', 'prod_decription']
    form_class = ProductsForm

class ProductsDelete(DeleteView):
    model = Products
    success_url = '/main'
    template_name = 'shop/delete.html'
    context_object_name = 'product'
    # fields = ['title', 'prod_decription']
    # form_class = ProductsForm

def create_prod(request):
    error = ''
    if request.method == "POST":
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_page')
        else:
            error = "something gone wrong..."
    form = ProductsForm()

    data = {
        'form':form,
        'error':error
    }
    return render(request, 'shop/create.html', data)