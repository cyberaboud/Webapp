from django import forms
from myapp.models import *

from django.forms import ModelForm

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ['num', 'nom', 'numChef', 'numAgendaDept']


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['numAgenda', 'dateCreation', 'numEmploye']


class DepartementForm(ModelForm):
    class Meta:
        model = Departement
        fields = '__all__'

class EmployeForm(ModelForm):
    class Meta:
        model = Employe
        fields = '__all__'


class ActivitesForm(ModelForm):
    class Meta:
        model = Activites
        fields = '__all__'