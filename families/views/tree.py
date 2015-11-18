# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from families.models import Relative
import json

#view for family tree
def tree(request):
    # return HttpResponse("<h1>Here will be my family's tree!!!</h1>")
    allRelatives = Relative.objects.all().order_by('id')

    data_my = [
        ['Year', 'Sales'],
        ['2004', 1000],
        ['2005', 1170],
        ['2006', 660]
    ]
    return render(request, 'families/tree.html', {'allRelatives': allRelatives,
                                                  'data_my': json.dumps(data_my)})
