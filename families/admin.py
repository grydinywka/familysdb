# -*- coding: utf-8 -*-

from django.contrib import admin
from django.forms import ModelForm, ValidationError

from .models import Relative

class RelativeFormAdmin(ModelForm):
    def clean_father(self):
        person = Relative.objects.filter(children_dad=self.cleaned_data['father'])
        if len(person) > 0 and self.instance in person:
            raise ValidationError(u'Син не може бути батьком свого рідного батька!', code="invalid")
        if self.cleaned_data['father'] == self.instance:
            raise ValidationError(u'Людина не може бути власним батьком!', code="invalid")

        return self.cleaned_data['father']

class RelativeAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'generation']
    form = RelativeFormAdmin

# Register your models here.
admin.site.register(Relative, RelativeAdmin)