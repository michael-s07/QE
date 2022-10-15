from django.shortcuts import render
from .models import Double_run_institution_woodin
from .forms import rsp1Form
# Create your views here.
def index(request):
    form = rsp1Form(request.POST or None)
    if form.is_valid():
        form.save()
        form = rsp1Form()

    context  = {
        'form' : form
    }

    return render(request, 'rsp1.html',context)

def rsp_list(request):
    object1 = Double_run_institution_woodin.objects.all()

    context = {
        'object1' : object1

    }
    return render(request, 'rsp_list.html', context)
