from django import forms
from django.contrib.auth.models import User
from gwalior.models import Complaints

class ComplaintsForm(forms.ModelForm):

	class Meta:
		model = Complaints
		exclude = ('solved', 'comment', 'preference')


class StatusForm(forms.Form):
    idnumber = forms.IntegerField()

    def clean_idnumber(self):
		idnumber = self.cleaned_data['idnumber']
		try:
			Complaints.objects.get(pk=idnumber)
			return idnumber
		except Complaints.DoesNotExist:
			raise forms.ValidationError("This Complaint ID doesn't exist. Enter Valid one !!")
		

# class UserForm(forms.ModelForm):
# 	password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput())
# 	password1 = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput())
# 	class Meta:
# 		model = User
# 		fields = ('username', 'email', 'password', 'password1')

# class UserProfileForm(forms.ModelForm):
# 	class Meta:
# 		model = UserProfile
# 		fields = ('first_name', 'last_name', 'address', 'area', 'pin', 'telephone', 'mobile', 'education', 'picture')