from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView

from account.forms import RegistrationForm, ProfileForm
from .models import Profile

class RegisterView(TemplateView):
	template_name = 'registration/register.html'
	form_class = RegistrationForm

	#def get_context_data()
	def post(self, request):

		form = self.form_class(request.POST)

		if form.is_valid():

			form.save()

			messages.add_message(request, messages.SUCCESS, "Account has been created successfully!!!")

			return HttpResponseRedirect('/login/?next=/')

		else:

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
	form_class = ProfileForm

	def get(self, request, *args):
		
		try:

			Profile.objects.get(user_id=request.user.id)
			flag = False

		except Profile.DoesNotExist:	

			flag = True

		return render(request, self.template_name, context={'flag': flag, 'form': self.form_class})
	

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['breadcrumbs'] = {
			'home': ('Home','account:signup'),
			#'account_cfg': ('Account Settings', 'login'),
			#'about': ('About', ''),
		}


		return context

