from django import forms

from .models import Photos

class PhotoForm(forms.ModelForm):
	class Meta:
		model = Upload
		docfile = forms.FileField(
        	label='Select a file'
    	)
		fields = [docfile]

	#def clean_email(self): #clean to overwrite email validation 
	#	email = self.cleaned_data.get('email')
	#	email_base, provider = email.split("@")
	#	domain, extension = provider.split('.')
	#	if not extension == "edu":
	#		raise forms.ValidationError("Plase use a valid .EDU email address")
	#	return email