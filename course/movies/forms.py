from django import forms
from .models import Reviews

class ReviwForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")