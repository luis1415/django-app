from django.shortcuts import render, redirect
from .models import Region, Commune
from .forms import RegionForm, CommuneForm


def list_regions(request):
    regions = Region.objects.all()
    communes = Commune.objects.all()
    return render(request, 'regions.html', {'regions': regions, 'communes': communes})


def create_region(request):

    form = RegionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_regions')
    
    return render(request, 'regions-form.html', {'form': form})


def update_region(request, id):
    region = Region.objects.get(id_region=id)
    form = RegionForm(request.POST or None, instance=region)
    if form.is_valid():
        form.save()
        return redirect('list_regions')
    
    return render(request, 'regions-form.html', {'form': form, 'region': region})


def delete_region(request, id):
    region = Region.objects.get(id_region=id)
    if request.method == 'POST':
        region.delete()
        return redirect('list_regions')

    return render(request, 'region-delete.html', context={"region": region})


def create_commune(request):

    form = CommuneForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_regions')
    
    return render(request, 'commune-form.html', {'form': form})


def update_commune(request, id):
    commune = Commune.objects.get(id_commune=id)
    form = CommuneForm(request.POST or None, instance=commune)

    if form.is_valid():
        form.save()
        return redirect('list_regions')
    
    return render(request, 'commune-form.html', {'form': form, 'commune': commune})


def delete_commune(request, id):
    commune = Commune.objects.get(id_commune=id)
    if request.method == 'POST':
        commune.delete()
        return redirect('list_regions')

    return render(request, 'commune-delete.html', context={"commune": commune})
    