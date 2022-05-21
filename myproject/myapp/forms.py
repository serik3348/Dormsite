from django import forms

from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Dormstudents
        fields = '__all__'



class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = '__all__'

