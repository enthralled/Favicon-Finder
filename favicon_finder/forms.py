from django import forms
from .models import Favicon


class FaviconForm(forms.ModelForm):
    get_fresh = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'id': 'get_fresh'
        })
    )

    class Meta:
        model = Favicon
        fields = ['url']
        widgets = {
            'url': forms.TextInput(attrs={
                'id': 'fav-url',
                'required': True,
                'placeholder': 'Find a favicon!'
            }),
        }
