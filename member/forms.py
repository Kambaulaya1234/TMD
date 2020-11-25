from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude=['created_at','is_member','has_fine']
        widgets = {
            'user': forms.Select(
                attrs={
                    "class": "form-control",
                    "style": "border-radius:50px",
                }
            ),
           
        }
