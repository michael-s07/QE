from django.shortcuts import render
from .forms import soaper_1Form, soaper_2Form, soaper_4Form, plain_DyeingForm
from .models import Soaper_1, Soaper_2, Soaper_4, Plain_Dyeing
# Create your views here.
def index(request):
    form1 = soaper_1Form(request.POST or None)
    if form1.is_valid():
        form1.save()
        form1 = soaper_1Form()

    form2 = soaper_2Form(request.POST or None)
    if form2.is_valid():
        form2.save()
        form2 = soaper_2Form()

    form3 = soaper_4Form(request.POST or None)
    if form3.is_valid():
        form3.save()
        form3 = soaper_4Form()

    form4 = plain_DyeingForm(request.POST or None)
    if form4.is_valid():
        form4.save()
        form4 = plain_DyeingForm()

    context = { 
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4

    }
    return render(request, 'alizarine.html', context)

def alizarine_list(request):
    object1 = Soaper_1.objects.all()
    object2 = Soaper_2.objects.all()
    object3 = Soaper_4.objects.all()
    object4 = Plain_Dyeing.objects.all()
    context = {
        'object1': object1,
        'object2': object2,
        'object3':object3,
        'object4':object4
    }
    return render(request, 'alizarine_list.html', context)