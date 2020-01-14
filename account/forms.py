from django import forms

from django.contrib.auth.models import User

from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.shortcuts import get_object_or_404
from django.contrib.auth import update_session_auth_hash

from account.models import Profile, MailClient, TrackingDetails
from datetime import date, timedelta, datetime

from django.contrib import messages
from django.core.mail import send_mail

PARISH = (
    ('', 'Choose...'),
    ('St. Andrew', 'Kingston'),
    ('Portland', 'St. Thomas'),
    ('St. Catherine', 'St. Mary'),
    ('St. Ann', 'Manchester',),
    ('Clarendon', 'Hanover',),
    ('Westmoreland', 'St. James',),
    ('Trelawny', 'St. Elizabeth')
)

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

		send_mail('Welcome to ShipEast!', '<h1>Welcome {}!</h1><br/><p>Your registered username is: {}<br/><br/>Our service is quick, effecient and reliable from we receive your package at<br/>our warehouse location to its delivery to you here in Jamaica</p>'.format(cd['first_name'],cd['username']), 'support@shipeastcouriers.com', [cd['email']])#, fail_silently=False)
		
		new_user = User.objects.create_user(username=cd['username'], first_name=cd['first_name'], last_name=cd['last_name'], email=cd['email'], password=cd['password'])

		new_user.save()

class TransactionForm(forms.ModelForm):

	class Meta:
		model = TrackingDetails
		fields = '__all__'
		
class TrackingForm(forms.Form):
	
	tracking_code = forms.CharField(max_length=50)

class ProfileFormUser(forms.Form):

	user = forms.IntegerField()
	date_of_birth = forms.DateField(input_formats=['%Y-%m-%d'],help_text='', widget=forms.DateInput(attrs={'class':'form-control','required':"", 'type': 'date',}))
	photo = forms.ImageField()
	trn = forms.CharField(max_length=10)
	address = forms.CharField(max_length=254)
	district = forms.CharField(max_length=254)
	parish = forms.ChoiceField(choices=PARISH)
	description = forms.CharField(max_length=254, widget=forms.Textarea(attrs={'rows':"3", 'cols':"140", 'resize':"none"}))
	

	def clean(self):
		cd = super(ProfileFormUser, self).clean()
		return cd
	
	def save(self, commit=True, uid=0):

		cd = self.cleaned_data

		if uid == 0:
	
			bio = Profile.objects.create(
				user_id=cd['user'],
				date_of_birth=cd['date_of_birth'],	
				photo=cd['photo'],	
				trn=cd['trn'],	
				address=cd['address'],	
				district=cd['district'],	
				parish=cd['parish'],	
				description=cd['description'],	
			)

		else:
			
			try:

				bio = Profile.objects.get(user_id=uid)
				bio.date_of_birth = cd['date_of_birth']
				bio.photo = cd['photo']
				bio.trn = cd['trn']
				bio.address = cd['address']
				bio.district = cd['district']
				bio.parish = cd['parish']
				bio.description = cd['description']

			except Profile.DoesNotExist:
				
				return False

			#super(ProfileFormUser, self).save(*args, **kwargs)
		if commit:
			bio.save()
		
		return bio

	class Meta:
		model = Profile
		fields= '__all__' #['date_of_birth', 'address', 'parish', 'description', 'photo', ]

class ProfileForm(forms.ModelForm):

    #user = forms.IntegerField()
	date_of_birth = forms.DateField(input_formats=['%Y-%m-%d'],help_text='', widget=forms.DateInput(attrs={'class':'form-control','required':"", 'type': 'date',}))
	photo = forms.ImageField()
	trn = forms.CharField(max_length=10)
	address = forms.CharField(max_length=254)
	district = forms.CharField(max_length=254)
	parish = forms.ChoiceField(choices=PARISH)
	description = forms.CharField(max_length=254, widget=forms.Textarea(attrs={'rows':"3", 'cols':"140", 'resize':"none"}))
	
	
	class Meta:
		model = Profile
		fields= '__all__' #['date_of_birth', 'address', 'parish', 'description', 'photo', ]


class EmailForm(forms.ModelForm):
	class Meta:
		model = MailClient
		fields = '__all__'