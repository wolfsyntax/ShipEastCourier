from django.contrib import admin

# Register your models here.
from account.models import MailClient
#from account.forms import EmailForm

from django import forms
from account.models import MailClient

class EmailClientForm(forms.ModelForm):
	
	class Meta:
		model = MailClient
		fields = ('subject','users','send_it',)

class EmailClientAdmin(admin.ModelAdmin):
    #exclude = ['age']
    form = EmailClientForm


admin.site.register(MailClient, EmailClientAdmin)