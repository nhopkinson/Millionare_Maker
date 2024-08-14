from django import forms
from users.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user_name','user_email','user_password']
