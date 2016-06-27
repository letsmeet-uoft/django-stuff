from .models import UserProfile
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(label='your password' ,widget=forms.PasswordInput())\

	class Meta:
		model = User
		fields = ('username', 'email', 'password',)
		widgets = {
			'username' : forms.TextInput(attrs={'placeholder' : 'Enter username'}), 
			'email' : forms.TextInput(attrs={'placeholder' : 'Enter email'}), 
			'password' : forms.TextInput(attrs={'placeholder' : 'Enter password'}),
		}

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('first_name', 'last_name',)
		widgets = {
			'first_name' : forms.TextInput(attrs={'placeholder' : 'Enter first name'}), 
			'last_name' : forms.TextInput(attrs={'placeholder' : 'Last name'}),
		}