from django.shortcuts import render
from .models import  *
from django.http import *
from .forms import *

def home(request):
    obj = student.objects.all().order_by('-date')
    return render(request, 'index.html', {'key':obj})

def student1(request):
    if request.method == 'POST':
        form = student_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/s/')

    else:
        form = student_form()
    return render(request, 'student.html', {'key2':form})
# Create your views here.
