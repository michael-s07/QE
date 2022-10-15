import re
from django.shortcuts import render
from .forms import woodin_institutionForm
from .models import Woodin_institution
# Create your views here.
def index(request):
    form1 = woodin_institutionForm(request.POST or None)
    if form1.is_valid():
        form1.save()
        form1 = woodin_institutionForm()

    context = {
        'form1':form1
    }

    return render(request, 'rsp23.html', context)

def rsp23_list(request):
    object1 = Woodin_institution.objects.all()

    context = {
        'object1':object1

    }
    return render(request, 'rsp23_list.html', context)