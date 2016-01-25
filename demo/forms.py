from django import forms
from django.forms import Form, CharField, Textarea, TextInput

class EditObjectForm(Form):
    # Object name
    attrs = {'readonly': 'readonly'}
    object_name = CharField(widget=TextInput(attrs=attrs))

    # Data
    attrs = {'autofocus': 'autofocus', 'required': 'true'}
    data = CharField(widget=Textarea(attrs=attrs))

class CreateObjectForm(Form):
    # Object name
    attrs = {'autofocus': 'autofocus', 'required': 'true'}
    object_name = CharField(widget=TextInput(attrs=attrs))

    # Data
    attrs = {'required': 'true'}
    data = CharField(widget=Textarea(attrs=attrs))

