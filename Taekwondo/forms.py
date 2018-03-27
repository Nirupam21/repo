from django import forms
from Taekwondo.models import Players
from django.forms import ModelForm

class PlayerForm(ModelForm):
    class Meta:
        model = Players
        fields = '__all__'
        db_table = 'Players'