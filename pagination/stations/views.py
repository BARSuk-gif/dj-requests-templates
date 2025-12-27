from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from pagination.settings import BUS_STATION_CSV


import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    all_stations = []
    with open(BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:   
        reader = csv.DictReader(csvfile)
        for row in reader:
            all_stations.append({
                'Name': row['Name'],
                'Street': row['Street'],
                'District': row['District']
            })
        
    paginator = Paginator(all_stations, 10)
    page_numer = int(request.GET.get("page", 1))    
    page_odj = paginator.get_page(page_numer)

    context = {
        'bus_stations': page_odj.object_list,
        'page': page_odj,
    }
    return render(request, 'stations/index.html', context)
