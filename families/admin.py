# -*- coding: utf-8 -*-

from django.contrib import admin
from django.forms import ModelForm, ValidationError

from .models import Relative, Surname

class RelativeFormAdmin(ModelForm):
    def clean_father(self):
        if self.cleaned_data['father'] is not None:
            person = Relative.objects.filter(children_dad=self.cleaned_data['father'])
        else:
            person = []
        if len(person) > 0 and self.instance in person:
            raise ValidationError(u'Син не може бути батьком свого рідного батька!, self.instance: {}, '
                                  u'self.cleaned_data[father]: {}'.format(self.instance, self.cleaned_data['father']),
                                  code="invalid")
        if self.cleaned_data['father'] == self.instance:
            raise ValidationError(u'Людина не може бути власним батьком!', code="invalid")

        return self.cleaned_data['father']

class RelativeAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_name', 'first_name', 'generation']
    form = RelativeFormAdmin

# Register your models here.
admin.site.register(Relative, RelativeAdmin)
admin.site.register(Surname)