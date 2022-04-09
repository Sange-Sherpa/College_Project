from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.CharField(required=True)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'required': '',
            'name': 'first_name',
            'id': 'first_name',
            'type': 'text',
            'placeholder': 'first name'
        })
        self.fields['last_name'].widget.attrs.update({
            'required': '',
            'name': 'last_name',
            'id': 'last_name',
            'type': 'text',
            'placeholder': 'last name'
        })
        self.fields['username'].widget.attrs.update({
            # 'required': '',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'placeholder': 'username'
        })
        self.fields['phone'].widget.attrs.update({
            'required': '',
            'name': 'phone',
            'id': 'phone',
            'type': 'text',
            'placeholder': 'phone number'
        })
        self.fields['password1'].widget.attrs.update({
            'required': True,
            'name': 'password1',
            'id': 'password1',
            'type': 'text',
            'placeholder': 'password'
        })
        self.fields['password2'].widget.attrs.update({
            'required': True,
            'name': 'password2',
            'id': 'password2',
            'type': 'text',
            'placeholder': 'confirm password'
        })

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'phone', 'password1', 'password2']