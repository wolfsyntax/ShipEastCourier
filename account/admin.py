from django.contrib import admin

# Register your models here.
from account.models import MailClient, TrackingDetails, Profile
from account.forms import TransactionForm
#from account.forms import EmailForm

from django import forms
#from account.models import MailClient, TrackingDetails
from datetime import date, timedelta

class EmailClientForm(forms.ModelForm):
	
	class Meta:
		model = MailClient
		fields = '__all__'#('subject','users','send_it',)

class EmailClientAdmin(admin.ModelAdmin):
    #exclude = ['age']
    form = EmailClientForm

class TransactionAdmin(admin.ModelAdmin):
    #exclude = ['age']
    form = TransactionForm

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('fullname','get_username','trn','date_of_birth', 'user_age','parish','district',)
	sortable_by = ['get_username', 'user_age','trn']
	search_fields = ['trn']

	def fullname(self, obj):
		return "{} {}".format(obj.user.first_name, obj.user.last_name)

	def user_age(self, obj):
		return (date.today()-obj.date_of_birth)//timedelta(days=365.2425)
	
	def get_username(self, obj):
		return "{}".format(obj.user.username)

	fullname.short_description='Name'
	user_age.short_description='Age'
	user_age.admin_order_field = 'birthdate'
	get_username.short_description='Username'

admin.site.register(MailClient, EmailClientAdmin)
admin.site.register(TrackingDetails, TransactionAdmin)
admin.site.register(Profile, ProfileAdmin)

admin.site.site_header = 'ShipEast Couriers Administration'
admin.site.empty_value_display = '(None)'
admin.site.index_title = "Administrator"
