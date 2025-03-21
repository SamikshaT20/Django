from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Product
from .forms import ProductForm
# Create your views here.
 
def home(request):
    if request.method == "POST":
        fm = ProductForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            fm = ProductForm()
    else:
        fm = ProductForm()

    prod = Product.objects.all()
    return render(request, 'clothing/home.html', {"prod":prod, "form":fm})


def update_data(request, id):
    pi = get_object_or_404(Product, pk=id)
    
    if request.method == "POST":
        fm = ProductForm(request.POST, request.FILES, instance=pi) 
        if fm.is_valid():
            fm.save()
            return redirect('home')  
        else:

            return render(request, 'clothing/update.html', {'form': fm})
    else:
        fm = ProductForm(instance=pi)
        return render(request, 'clothing/update.html', {'form': fm})

    
def delete_data(request, id):
    if request.method == "POST":
        pi = Product.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")