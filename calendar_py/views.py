from django.shortcuts import render
from .calendar import Calendar, Custody

def calendar(request):
    year = 2015
    month = 10
    calendar = Calendar(year, month)
    return render(request, 'index.html', {'calendar': calendar})

