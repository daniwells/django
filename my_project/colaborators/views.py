from django.shortcuts import render, redirect, get_object_or_404
from .models import Colaborator
from .forms import ColaboratorForm
from PIL import Image
import copy
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


def show_colaborators(request):
    colaborators = Colaborator.objects.all()
    return render(request, 'colaborators/show_colaborators.html', {'colaborators': colaborators})

@csrf_exempt
def register_colaborator(request):
    if request.method == 'POST':
        
        file = request.FILES.get("perfil_image")
        img = Image.open(file)
        path = os.path.join(settings.BASE_DIR, f"media/{file.name}")
        
        post = copy.deepcopy(request.POST) 
        post["perfil_image"] = path
        form = ColaboratorForm(post)
        
        if form.is_valid():
            img.save(path)    
            form.save()
            return redirect('colaborators:show_colaborators')
    else:
        form = ColaboratorForm()
    return render(request, 'colaborators/register_colaborator.html', {'form': form})

def edit_colaborator(request, pk):
    cliente = get_object_or_404(Colaborator, pk=pk)
    if request.method == 'POST':
        form = ColaboratorForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('colaborators:show_colaborators')
    else:
        form = ColaboratorForm(instance=cliente)
    return render(request, 'colaborators/edit_colaborator.html', {'form': form})

def delete_colaborator(request, pk):
    cliente = get_object_or_404(Colaborator, pk=pk)
    cliente.delete()
    return redirect('colaborators:show_colaborators')


