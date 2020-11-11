from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserCreateForm(forms.ModelForm):
    class Meta:
        model=User
        # fields='__all__'

        exclude=[
        'date_joined','is_active','last_login','password',
        'is_superuser','is_staff','user_permissions',
        ]

        labels={
            'first_name':'',
            'email':'',
            'username':'',
            'last_name':'',
            'password':'',
            'groups':'',
        }
        widgets={
            'first_name':forms.TextInput(
                attrs={
                'class':"form-control",
                'placeholder':"Enter firstname",
                }
            ),
            'last_name':forms.TextInput(
                attrs={
                'class':"form-control",
                'placeholder':"Enter you last name",
                }
            ),
            'username':forms.TextInput(
                attrs={
                'class':"form-control",
                'placeholder':"Enter username",
                }
            ),
            'email':forms.EmailInput(
                attrs={
                'class':"form-control",
                'placeholder':"Enter email",
                }
            ),
           
            'groups':forms.Select(
                attrs={
                'class':"form-control",
                'placeholder':"Select groups",
                }
            ),
        }

