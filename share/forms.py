from django import forms
from .models import Share
from member.models import Member
from django.conf import settings
from django.contrib.auth.models import User
# User=settings.AUTH_USER_MODEL

class CreateShareForm(forms.ModelForm):
    member = forms.ModelChoiceField(
        queryset=Member.objects.filter(is_member=True,has_fine=False), empty_label='-----Select Member----', widget=forms.Select(
        attrs={
            'class': 'form-control',
            'style': 'border-radius: 20px',
        }
    ))

    class Meta:
        model = Share
        exclude = ['created_at','fine']
        widgets = {
            'week': forms.Select(
                attrs={
                    "class": "form-control",
                    "style": "border-radius:50px",
                }
            ),
            'year': forms.Select(
                attrs={
                    "class": "form-control",
                    "style": "border-radius:50px",
                }
            ),
            'month': forms.Select(
                attrs={
                    "class": "form-control",
                    "style": "border-radius:50px",
                }
            ),
            'hisa': forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your share 1,2,3...",
                    "style": "border-radius:50px",
                }
            ),
            'jamii': forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your user...",
                    "style": "border-radius:50px",
                }
            ),
            'mbebeo': forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your user...",
                    "style": "border-radius:50px",
                }
            ),
            'marejesho': forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your user...",
                    "style": "border-radius:50px",
                }
            ),
            'starting': forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your user...",
                    "style": "border-radius:50px",
                }
            ),

        }
