from .forms import RegistrationForm
from django.http import HttpResponseRedirect 
from django.shortcuts import render
from .models import *
def regisiter(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'home/form_dangki.html', {'form': form})


def getAbout(request):
    context ={ }
    return render(request,'home/about.html',context)

def getHome(request):
    products = product.objects.all()[:4]
    context ={'products':products}
    rows_of_products = []
    current_row = []
    return render(request,'home/home1.html',context)

def cart(request):
    context ={ }
    return render(request,'home/cart.html',context)

