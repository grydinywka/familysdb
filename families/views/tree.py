# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

#view for family tree
def tree(request):
    # return HttpResponse("<h1>Here will be my family's tree!!!</h1>")
    return render(request, 'families/tree.html', {})
