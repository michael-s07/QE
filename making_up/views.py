from django.shortcuts import render
from .forms import finishing_PiecesForm
from .models import Finishing_Pieces
from django.contrib import messages
# Create your views here.
def index(request):
    if (str(request.user) is 'AnonymousUser'):
        messages.success(request, ("Please Log in"))
    else:
        messages.success(request, ("Welcome"))

    
    

    form1 = finishing_PiecesForm(request.POST or None)
    if form1.is_valid():
        form1.save()
        form1 = finishing_PiecesForm()
        messages.success(request, ("Data was Entered Successfully"))

    context= {'form1': form1}
    return render(request, 'making.html', context)


def making_list(request):
    obj = Finishing_Pieces.objects.all()

    context = {
        'object': obj

    }
    return render(request, 'admin_view.html', context)