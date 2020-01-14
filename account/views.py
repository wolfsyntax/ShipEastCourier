from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView

from account.forms import RegistrationForm, ProfileForm, ProfileFormUser
from .models import Profile, TrackingDetails

class RegisterView(TemplateView):
	template_name = 'registration/register.html'
	form_class = RegistrationForm

	#def get_context_data()
	def post(self, request):

		form = self.form_class(request.POST)
		
		message = ""
		flag = True

		if form.is_valid():

			form.save()

			messages.add_message(request, messages.SUCCESS, "Account has been created successfully!!!")
			#message = "Account has been created successfully!"
			return HttpResponseRedirect('/login/?next=/')

		else:
			#flag = False
			#message = "Please fillup the form"
			messages.add_message(request, messages.ERROR, "Please fillup the form")

		return render(request, self.template_name, {"form": form})

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)
		context['form'] = self.form_class
		
		return context

class TestView(TemplateView):
	
	template_name = "account/customer/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['breadcrumbs'] = {
			'home': ('Home','account:signup'),
			'warehouse': ('Warehouse','account:signup'),
			'inventory': ('Inventory','login'),
			'shipment': ('Shipment','account:signup'),
			'order': ('Orders', 'account:signup'),
			'invoice': ('Invoices', 'login'),
		}
		
		return context

class Test2View(TemplateView):
	
	template_name = "account/customer/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['breadcrumbs'] = {
			'home': ('Home','account:signup'),
			'account_cfg': ('Account Settings', 'login'),
			'about': ('About', ''),
		}
		
		return context

class DashboardView(LoginRequiredMixin, TemplateView):
	
	template_name = "account/customer/index.html"
	form_class = ProfileFormUser
	success_url ="/"

	def form_valid(self, form):
		form.save()
		print("\n\n\n\n\n\n\n\n\nUpdate Form Is Valid\n\n\n\n\n\n\n\n\n")
		return redirect(self.success_url )

	def post(self, request, *args, **kwargs):
		form =  self.form_class(request.POST, request.FILES)
		
		if form.is_valid():
			form.save()
		#	print("\n\n\n\n\n\n\n\n\nUpdate Form Is Valid\n\n\n\n\n\n\n\n\n")
				
		return HttpResponseRedirect('/dashboard')
			
	def get(self, request, *args):
		
		breadcrumbs = {
			'home': ('Home','account:signup'),
			#'account_cfg': ('Account Settings', 'login'),
			#'about': ('About', ''),
		}
		#print("\n\n\n\nSAMPLE CONTEXTDATA\n\n{}\n\n\n\n".format(request.user.id))
		try:

			Profile.objects.get(user_id=request.user.id)
			flag = False

		except Profile.DoesNotExist:	

			flag = True


		try:

			unrecord = TrackingDetails.objects.filter(user_id=request.user.id) #all() #filter(user_id=request.user.id)
			iflag = True

		except TrackingDetails.DoesNotExist:
			
			iflag = False
			unrecord = None	
			
		#print("iFlag: {}\n\n\n\n".format(iflag))

		return render(request, self.template_name, context={'flag': flag, 'form': self.form_class, 'invoice':unrecord, 'inflag':iflag, 'breadcrumbs': breadcrumbs})
	

	#def get_context_data(self, **kwargs):
	#	context = super().get_context_data(**kwargs)
	#	print("\n\n\n\nSAMPLE CONTEXTDATA\n\n{}\n\n\n\n".format(request.user.id))
	#	context['breadcrumbs'] = {
	#		'home': ('Home','account:signup'),
	#		#'account_cfg': ('Account Settings', 'login'),
	#		#'about': ('About', ''),
	#	}




		return context

