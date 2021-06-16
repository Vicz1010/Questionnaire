from django import forms
from Myapp.models import NewForm

class MyForm(forms.ModelForm):
    class Meta():
        model = NewForm
        fields = '__all__'