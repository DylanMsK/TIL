from django import forms
from .models import Shout

class ShoutForm(forms.Form):
    title = forms.CharField(max_length=30)
    content = forms.CharField(max_length=100)


class ShoutModelForm(forms.ModelForm):
    class Meta:
        model = Shout
        fields = '__all__'

        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }