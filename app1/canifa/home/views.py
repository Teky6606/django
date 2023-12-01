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
    return render(request, 'home/home.html', {'form': form})