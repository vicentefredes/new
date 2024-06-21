from django.shortcuts import render

# Create your views here.
def index(request):
    context={'clase':'index'}
    return render(request, 'demo/index.html', context)

def galeria(request):    
    context={'clase':'galeria'}
    return render(request, 'demo/galeria.html', context)