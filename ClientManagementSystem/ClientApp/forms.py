from django import forms
from .models import ClientModel


class ClientForm (forms.ModelForm):
    class Meta:
        model=ClientModel
        fields='__all__'