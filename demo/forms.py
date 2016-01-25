from django import forms
from django.forms import Form, CharField, Textarea, TextInput

class EditObjectForm(Form):
    # Object name
    attrs = {'readonly': 'readonly'}
    object_name = CharField(widget=TextInput(attrs=attrs))

    # Data
    attrs = {'autofocus': 'true'}
    data = CharField(widget=Textarea(attrs=attrs))

class CreateObjectForm(Form):
    # Object name
    attrs = {'autofocus': 'true'}
    object_name = CharField(widget=TextInput(attrs=attrs))

    # Data
    data = CharField(widget=Textarea())

