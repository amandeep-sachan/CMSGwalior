from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from registrations.models import UserProfiles

class RegistrationForm(ModelForm):
	username = forms.CharField(label=(u'User Name'))
	email = forms.EmailField(label=(u'Email Address'))
	password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
	password1 = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))

	class Meta:
		model = UserProfiles
		exclude = ('user',)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError("That username is already taken, please select another.")

	def clean_mobile(self):
		mobile = self.cleaned_data['mobile']
		try:
			UserProfiles.objects.get(mobile=mobile)
		except UserProfiles.DoesNotExist:
			return mobile
		raise forms.ValidationError("This Mobile Number is already registered.")

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError("This Email-id is already registered.")

	def clean_password1(self):
		password = self.cleaned_data['password']
		password1 = self.cleaned_data['password1']
		if password != password1:
			raise forms.ValidationError("The passwords did not match. Please try again.")
		return self.cleaned_data

class LoginForm(forms.Form):
	username = forms.CharField(label=(u'User Name'))
	password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
