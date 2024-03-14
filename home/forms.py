from django import forms
from .models import Member

class MemberForm(forms.Form):
    memb_name = forms.CharField()
    memb_email = forms.CharField()