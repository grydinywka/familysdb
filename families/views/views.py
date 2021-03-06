# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

#View for information
def info(request):
    return render(request, 'families/home.html', {})

#Views for relatives

def relatives_list(request):
    relatives = (
        {'id': 1,
         'first_name': u'Сергій',
         'last_name': u'Ігнатенко',
         'sex': u'Ч',
         'photo': 'img/sergiy.JPG',
         'family': [u'Ігнатенко Микола', u'Ігнатенко(Пономарьова) Тетяна', u'Ігнатенко Надія'],
         'generation': 0},
        {'id': 2,
         'first_name': u'Софія',
         'last_name': u'Пелипецька',
         'sex': u'Ж',
         'photo': 'img/sofiya.JPG',
         'family': [u'Пелипецький Руслан', u'Ігнатенко Надія'],
         'generation': 1},
        {'id': 3,
         'first_name': u'Вікторія',
         'last_name': u'Ігнатенко',
         'sex': u'Ж',
         'photo': 'img/vika.JPG',
         'family': [u'Ігнатенко Віктор', u'Ігнатенко(Сливко) Оля', u'Ігнатенко Марина'],
         'generation': 0}
    )

    return render(request, 'families/relatives_list.html', {'relatives': relatives})

def relatives_add(request):
    return HttpResponse('<h1>Additing relative</h1>')

def relatives_edit(request, rid):
    return HttpResponse('<h1>Editing relative # %s!</h1>' % rid)

def relatives_native(request, rid):
    return HttpResponse("<h1>Show native's cell of %s relative!</h1>" % rid)

def relatives_info(request, rid):
    return HttpResponse("<h1>Information about %s relative</h1>" % rid)

def relatives_delete(request, rid):
    return HttpResponse("<h1>Delete %s relative!</h1>" % rid)

#VIEWS FOR GENERATIONS

def generations_list(request):
    return HttpResponse('<h1>Generations Listing</h1>')

#view for family tree
def tree(request):
    return HttpResponse("<h1>Here will be my family's tree!!!</h1>")
