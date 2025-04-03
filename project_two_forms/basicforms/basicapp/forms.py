from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    bot_catcher = forms.CharField(required=False,widget=forms.HiddenInput)