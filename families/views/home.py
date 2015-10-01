# -*- coding: utf-8 -*-

from django.shortcuts import render
from families.models import Surname

#View for information
def home(request):
    surnames = Surname.objects.all()
    valueSur = surnames.count()
    return render(request, 'families/home.html', {'surnames1': surnames[:valueSur/2],
                                                  'surnames2': surnames[valueSur/2:]})