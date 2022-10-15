from django.shortcuts import render
from .forms import stenter_5Form, stenter_7Form, calenderForm, bakingOvenForm
from .models import Stenter_5, Stenter_7, Calender, Baking_Oven
# Create your views here.
def index(request):
    form1 = stenter_5Form(request.POST or None)
    if form1.is_valid():
        form1.save()
        form1 = stenter_5Form()

    form2 = stenter_7Form(request.POST or None)
    if form2.is_valid():
        form2.save()
        form2 = stenter_7Form()

    form3 = calenderForm(request.POST or None)
    if form2.is_valid():
        form2.save()
        form2 = calenderForm()

    form4 = bakingOvenForm(request.POST or None)
    if form2.is_valid():
        form2.save()
        form2 = bakingOvenForm()

    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4

    }
    return render(request, 'finish.html', context)


def finish_list(request):
    object1 = Stenter_5.objects.all()
    object2 = Stenter_7.objects.all()
    object3 = Calender.objects.all()
    object4 = Baking_Oven.objects.all()

    context  = {
        'object1' : object1,
        'object2' : object2,
        'object3' : object3,
        'object4' : object4
     
    }
    return render(request, 'finish_list.html', context)