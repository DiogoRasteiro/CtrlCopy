from django import forms
from plagiarism.models import Document

class DocumentForm(forms.Form):
    file = forms.FileField()

class LoginForm(forms.Form):
    email = forms.CharField(label = 'email', max_length=100)
    password = forms.CharField(label = 'email', max_length=100)

class AnalyzeForm(forms.Form):
    percentage_level = forms.IntegerField(label = 'percentage_level')
