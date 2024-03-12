# from django.shortcuts import render
# from django.http import HttpResponse

from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm

# def members(request):
#     return HttpResponse("Hello world!")
# Create your views here.

def list_client(request):
    clients = Client.objects.all()
    return render(request, 'clients/list_client.html', {'clients':clients})

def make_client(request):
    print(request.method)
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_client')
    else:
        form = ClientForm()
    return render(request, 'clients/make_client.html', {'form': form})
        
def edit_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("list_client")
        
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/edit_client.html', {'form': form})

def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('list_client')

