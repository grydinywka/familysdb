# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

#VIEWS FOR GENERATIONS

def generations_list(request):
    generations_rachuk = (
        {'id': 1,
         'relatives': [u'Пелипецька Софія', u'Ігнатенко Богдан']},
        {'id': 0,
         'relatives': [u'Ігнатенко Марина', u'Ігнатенко Максим', u'Шпилька Дмитро']}
    )

    generations_ignatenko = ()

    generations_ponomariov = ()

    generations_lisitsina = ()

    main_relatives = (
        {'person': u'По Надії Свиридівні Ігнатенко',
         'generations': generations_rachuk},
        { 'person': u'По Костянтину Івановичу Ігнатенко',
          'generations': generations_ignatenko},
        {'person': u'По Антоніні Пономарьовій',
         'generations': generations_lisitsina},
        { 'person': u'По Іллічу Пономарьову',
          'generations': generations_ponomariov}
    )

    return render(request, 'families/generations_list.html', {'main_relatives': main_relatives})

# def generation_
