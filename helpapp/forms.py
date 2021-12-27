from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatch = forms.CharField(required=False,widget=forms.HiddenInput)

    def clean_botcatch(self):
        botcatch = self.cleaned_data['botcatch']
        if len(botcatch) > 0:
            raise forms.ValidationError('This is a Bot!! :(')
        return botcatch
