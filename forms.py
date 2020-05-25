from django import forms
from SecondApp.models import Users


class FormName(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    second_name = forms.CharField()

    class Meta:
        model = Users
        fields = ['email', 'first_name', 'second_name']
