from django.forms import ModelForm
from django import forms
from django.forms import DateInput
from .models import *
from .views import *

class FormServico(ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'

class FormServicoDia(ModelForm):
    class Meta:
        model = Servico_dia
        fields = '__all__'