from django.shortcuts import render
from  .forms import singelingForm, desizing_mangleForm, merceriserForm, stenter_6Form
from .models import Singeing, Desizing_mangle, Merceriser, Stenter_6
from django.http import HttpResponse
# Create your views here.
def index(request):
    #template = loader.get_template('pretrement/index.html')
    
    form1 =  singelingForm(request.POST or None)
    if form1.is_valid():
        form1.save()
        form1 = singelingForm()

    form2 =  desizing_mangleForm(request.POST or None)
    if form2.is_valid():
        form2.save()
        form2 = desizing_mangleForm()

    form3 =  merceriserForm(request.POST or None)
    if form3.is_valid():
        form3.save()
        form3 = merceriserForm()

    form4 =  stenter_6Form(request.POST or None)
    if form4.is_valid():
        form4.save()
        form4 = stenter_6Form()
    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4
    }
    return render(request, 'index.html', context)

def pretreatment_list(request):
    object1 = Singeing.objects.all()
    object2 = Desizing_mangle.objects.all()
    object3 = Merceriser.objects.all()
    object4 = Stenter_6.objects.all()

    context = {
        'object1': object1,
        'object2': object2,
        'object3': object3,
        'object4': object4

    }
    return render(request, "pre_list.html", context)