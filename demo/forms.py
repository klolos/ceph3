from django import forms

class EditObjectForm(forms.Form):
    data_widget = forms.Textarea(
                    attrs={'required': 'true',
                           'autofocus': 'true'})
    data = forms.CharField(widget=data_widget)

class CreateObjectForm(forms.Form):
    data_widget = forms.Textarea(attrs={'required': 'true'})
    data = forms.CharField(widget=data_widget, required=True)

    name_widget = forms.TextInput(attrs={'required': 'true',
                                         'autofocus': 'true'})
    object_name = forms.CharField(widget=name_widget, required=True)

