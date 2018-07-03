from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import ObjectDoesNotExist
from .models import Mineral
import random
import string

# Create your views here.
def index(request):
    minerals = Mineral.objects.all()
    return render(request, 'catalog/home.html', {'minerals': minerals})

def detail(request, pk):
    try:
        mineral = Mineral.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return redirect('/')
    return render(request, 'catalog/detail.html', {'mineral': mineral})

def random_mineral(request):
    count = len(Mineral.objects.all())
    pk = round(random.randint(0, count))
    try:
        mineral = Mineral.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return redirect('/')
    return render(request, 'catalog/detail.html', {'mineral': mineral})

def search(request):
    term = request.GET.get('q', '')
    minerals = Mineral.objects.filter(name__icontains=term)
    return render(request, 'catalog/home.html', {'minerals': minerals})

def filter_by_letter(request):
    l = request.GET.get('l', '')
    minerals = Mineral.objects.filter(name__istartswith=l)
    return render(request, 'catalog/home.html', {'minerals': minerals, 'selected_letter': l.upper()})

def group(request):
    g = request.GET.get('g', '')
    minerals = Mineral.objects.filter(fields__icontains='\"group\": \"{}\"'.format(g))
    return render(request, 'catalog/home.html', {'minerals': minerals, 'selected_group': g})