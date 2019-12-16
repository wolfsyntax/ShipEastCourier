from django import forms

from django.contrib.auth.models import User

from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.shortcuts import get_object_or_404
from django.contrib.auth import update_session_auth_hash

from .models import Profile
from datetime import date, timedelta, datetime

from django.contrib import messages
from django.core.mail import send_mail

class RegistrationForm(forms.ModelForm):
	
	confirm_password = forms.CharField()

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password']
#    date_of_birth = forms.DateField(blank=True, null=True)
#    photo = forms.ImageField(upload_to='users/%Y/%m/%d', blank=True)
#    address = forms.CharField(max_length=254)
#    parish = forms.CharField(choices=PARISH, max_length=15)
	
#    description = forms.CharField(max_length=255, blank=True)
	

	def clean(self):
		cd = super(RegistrationForm, self).clean()
		passwd = self.cleaned_data['password']
		confirm_password = self.cleaned_data['confirm_password']

		if passwd != confirm_password:
			self.add_error('confirm_password', 'Confirm Password not match.')

		return cd

	def clean_username(self):
        # Get the email
		uname = self.cleaned_data.get('username', '')

		try:
			match = User.objects.get(username=uname)

		except User.DoesNotExist:
            # Unable to find a user, this is fine
			return uname

        # A user was found with this as a username, raise an error.
		raise forms.ValidationError('Username is already in use.')

	def save(self):
		
		cd = self.cleaned_data

		send_mail('Welcome to ShipEast!', '<h1>Welcome {}!</h1><br/><p>Your registered username is: {}<br/><br/>Our service is quick, effecient and reliable from we receive your package at<br/>our warehouse location to its delivery to you here in Jamaica</p>'.format(cd['first_name'],cd['username']), 'support@shipeastcouriers.com', ['jaysonalpe@gmail.com', 'shipeast85@gmail.com', 'developer@shipeastcouriers.com' 'cnegro@gbox.adnu.edu.ph'])#, fail_silently=False)
		
		new_user = User.objects.create_user(username=cd['username'], first_name=cd['first_name'], last_name=cd['last_name'], email=cd['email'], password=cd['password'])

		new_user.save()

class TrackingForm(forms.Form):
	
	trackcode = forms.CharField(max_length=50)

class ProfileForm(forms.ModelForm):
	
	description = forms.CharField(max_length=254, widget=forms.Textarea(attrs={'rows':"3", 'cols':"140", 'resize':"none"}))
	address = forms.CharField(max_length=254)
	date_of_birth = forms.DateField(input_formats=['%Y-%m-%d'],help_text='', widget=forms.DateInput(attrs={'class':'form-control','required':"", 'type': 'date',}))
	class Meta:
		model = Profile
		fields=['date_of_birth', 'address', 'parish', 'description', 'photo', ]
