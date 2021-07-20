from django import forms
from django.forms.widgets import TextInput,PasswordInput



class LoginForm(forms.Form):

	username = forms.CharField(widget=forms.TextInput)
	password = forms.CharField(widget=forms.PasswordInput)