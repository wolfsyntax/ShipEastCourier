from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView
from account.forms import RegistrationForm

from django.contrib import messages

class RegisterView(TemplateView):
	template_name = 'registration/register.html'
	form_class = RegistrationForm

	#def get_context_data()
	def post(self, request):

		form = self.form_class(request.POST)

		if form.is_valid():

			form.save()

			messages.add_message(request, messages.SUCCESS, "Account has been created successfully!!!")

			return HttpResponseRedirect('/login?next=/')
		else:
			messages.add_message(request, messages.ERROR, "Please fillup the form")
		return render(request, self.template_name, {"form": form})

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = self.form_class
		
		return context