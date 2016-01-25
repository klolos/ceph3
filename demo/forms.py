from django import forms

class EditObjectForm(forms.Form):
    data = forms.CharField(widget=forms.Textarea)

class CreateObjectForm(forms.Form):
    data = forms.CharField(widget=forms.Textarea)
    object_name = forms.CharField()

