from .forms import RegistrationForm
from django.http import HttpResponseRedirect 
from django.shortcuts import render
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
    context ={ }
    return render(request,'home/home1.html',context)