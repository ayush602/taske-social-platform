from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from django import forms

# creating a form
class InputForm(forms.Form):

	mobile_number = forms.IntegerField()
	email = forms.EmailField()
	name = forms.CharField(max_length=20)
	password = forms.CharField(widget = forms.PasswordInput())

class LInputForm(forms.Form):

	lmobile_number = forms.IntegerField()
	lpassword = forms.CharField(widget = forms.PasswordInput())
