from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
from .forms import DegreeForm
from django.conf import settings

def search(request):
    return render(request, 'api/search.html')


def degree_list(request):
    degrees = Degree.objects.filter(date_degree__lte=timezone.now()).order_by('date_degree')
    return render(request, 'api/degree_list.html', {'degrees': degrees})


def search_result(request):
    query = request.GET.get('search_text')
    if query:
        degrees = Degree.objects.filter(hash__exact=query)
        return render(request, 'api/search_result.html', {'degrees': degrees, 'query': query})
    else:
        degrees = Degree.objects.none()
        return render(request, 'api/search_result.html', {'degrees': degrees})


def degree_detail(request, pk):
    degree = get_object_or_404(Degree, pk=pk)
    degree_txId = degree.txId
    link = f"https://sepolia.etherscan.io/tx/{degree_txId}"
    return render(request, 'api/degree_detail.html', {'degree': degree, 'link': link})


def degree_new(request):
    if request.method == "POST":
        form = DegreeForm(request.POST)
        if form.is_valid():
            degree = form.save(commit=False)
            degree.user = request.user
            degree.date_degree = degree.date_degree
            degree.writeOnChain()
            degree.save()
            return redirect('degree_detail', pk=degree.pk)
    else:
        form = DegreeForm()
    return render(request, 'api/degree_edit.html', {'form': form})


def degree_edit(request, pk):
    degree = get_object_or_404(Degree, pk=pk)
    if request.method == "POST":
        form = DegreeForm(request.POST, instance=degree)
        if form.is_valid():
            degree = form.save(commit=False)
            degree.user = request.user
            degree.date_degree = degree.date_degree
            degree.writeOnChain()
            degree.save()
            return redirect('degree_detail', pk=degree.pk)
    else:
        form = DegreeForm(instance=degree)
    return render(request, 'api/degree_edit.html', {'form': form})


