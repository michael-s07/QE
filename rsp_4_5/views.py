from django.shortcuts import render
from .forms import adepa_Base_Nustyle_SafoaForm, steamerForm, owsForm
from .models import Adepa_Base_Nustyle_Safoa, Steamer, OWS
# Create your views here.
def index(request):
    form1 = adepa_Base_Nustyle_SafoaForm(request.POST or None)
    if form1.is_valid():
        form1.save()
        form1 = adepa_Base_Nustyle_SafoaForm()

    form2 = steamerForm(request.POST or None)
    if form2.is_valid():
        form2.save()
        form2 = steamerForm()

    form3 = owsForm(request.POST or None)
    if form3.is_valid():
        form3.save()
        form3 = owsForm()
        
    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3
        }
    return render(request, 'rsp45.html', context)

def rsp45_list(request):
    object1 = Adepa_Base_Nustyle_Safoa.objects.all()
    object2 = Steamer.objects.all()
    object3 = OWS.objects.all()


    context = {
        'object1':object1,
        'object2':object2,
        'object3':object3

    }
    return render(request, 'rsp45_list.html', context)