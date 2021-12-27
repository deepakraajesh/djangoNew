from django import forms
from django.core.exceptions import ValidationError

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to Start with Z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatch = forms.CharField(required=False,widget=forms.HiddenInput)

    def clean_botcatch(self):
        botcatch = self.cleaned_data['botcatch']
        if len(botcatch) > 0:
            raise forms.ValidationError('This is a Bot!! :(')
        return botcatch
