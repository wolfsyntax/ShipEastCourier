from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView
# Create your views here.
from django.core.mail import send_mail

from account.forms import TrackingForm

class HomeView(TemplateView):
	template_name = 'sitemap/index.html'

class AboutView(TemplateView):
	template_name = 'sitemap/about.html'	

class ContactView(TemplateView):
	template_name = 'sitemap/contact.html'
	#send_mail('Test','This is a sample mail','support@shipeastcouriers.com',['jaysonalpe@gmail.com'])
	
	def get(self, request):
		send_mail('Subject here', 'Here is the message.', 'support@shipeastcouriers.com', ['jaysonalpe@gmail.com'])#, fail_silently=False)

class FAQView(TemplateView):
	template_name = 'sitemap/faq.html'

class ServiceView(TemplateView):
	template_name = 'sitemap/services.html'

class TrackParcelView(TemplateView):
	
	template_name = 'sitemap/tracking.html'
	form_class = TrackingForm

	def post(self, request):
		
		form = self.form_class(request.POST)
		if form.is_valid():
			print("\n\n\n\nTrackParcel\nTracking Code: {}\n\n".format(request.POST['trackcode']))
			
			return HttpResponseRedirect("/track/{}".format(request.POST['trackcode']))

		return HttpResponseRedirect("/track")

	def get_context_data(self,**kwargs):

		context = super().get_context_data(**kwargs)
		
		if(kwargs):
		
			print("\n\n\n\n\nTracking Code:\n{}-1\n\n\n".format(kwargs['tracking_code']))

		return context