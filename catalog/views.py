from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'catalog/home.html', {'minerals': []})

def detail(request, pk):
    return render(request, 'catalog/detail.html')