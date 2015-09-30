# -*- coding: utf-8 -*-

from django.shortcuts import render

#View for information
def info(request):
    return render(request, 'families/home.html', {})