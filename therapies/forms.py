# # coding: utf-8
# from django import forms
# from .models import Therapie, Time


# class TherapieForm(forms.ModelForm):
#     class Meta:
#         model = Therapie
#         fields = ['doctors', 'terapy', ]


# class TimeInlineFormset(forms.models.BaseInlineFormSet):

#     def clean(self):
#         # get forms that actually have valid data
#         featured = 0
#         featured_cover = 0
#         errors = []

#         for form in self.forms:

#             if form.cleaned_data:

#                 if form.cleaned_data['featured_internal'] == True:
#                     featured += 1
#                 if form.cleaned_data['featured_cover'] == True:
#                     featured_cover += 1


#         if featured > 1:
#             errors.append('Você deve escolher apenas uma foto de destaque.')
#         if featured < 1:
#             errors.append('Você deve escolher  uma foto de destaque.')

#         if featured_cover > 1:
#             errors.append('Você deve escolher apenas uma foto de capa.')
#         if featured_cover < 1:
#             errors.append('Você deve escolher uma foto de capa.')
#         raise forms.ValidationError(errors)
