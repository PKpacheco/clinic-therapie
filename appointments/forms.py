from django import forms
from .models import Appointment


# WD = (
#     ('seg', 'segunda'),
#     ('ter', 'terca')
# )


# class AppointmentForm(forms.BaseModelForm):

#     year = forms.ChoiceField(choices=WD, required=False)

#     def __init__(self, *args, **kwargs):
#         super(AppointmentForm, self).__init__(*args, **kwargs)
#         self.fields['year'].queryset = WD.objects.none()
#         self.fields['year'].widget = forms.TextInput(attrs={'placeholder': _(u'Select Year')})
