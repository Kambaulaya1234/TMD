from django import forms
from django.contrib.auth.models import Group



class GroupCreateForm(forms.ModelForm):
    class Meta:
        model=Group
        fields=['name']
        labels={
            'name':''
        }
        widgets={
            'name':forms.TextInput(
                attrs={
                'class':"form-control",
                'placeholder':"Enter The name of your group",
                }
            )
        }
