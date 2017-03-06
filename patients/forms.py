# coding: utf-8


from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from patients.models import Person, Child


class ResponsibleForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['name', 'email', 'dni', 'primary_contact_phone', 'cellphone', 'telephone']

        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'})
        # }


class ChildForm(forms.ModelForm):

    class Meta:
        model = Child
        fields = ['name', 'age']


ChildFormSet = inlineformset_factory(Person, Child, form=ChildForm, extra=3)
