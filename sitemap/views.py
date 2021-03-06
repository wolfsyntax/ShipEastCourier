from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView
# Create your views here.
from django.core.mail import send_mail

from account.forms import TrackingForm
from account.models import TrackingDetails

class HomeView(TemplateView):
	template_name = 'sitemap/index.html'

class AboutView(TemplateView):
	template_name = 'sitemap/about.html'	

class ContactView(TemplateView):
	template_name = 'sitemap/contact.html'
	#send_mail('Test','This is a sample mail','support@shipeastcouriers.com',['jaysonalpe@gmail.com'])
	
	def get(self, request):
		#send_mail('Welcome to ShipEast', 'Hello, World! This is just a sample email.', 'info@shipeastcouriers.com', ['jaysonalpe@gmail.com'])#, fail_silently=False)
		return render(request, self.template_name)

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
			#print("\n\n\n\nTrackParcel\nTracking Code: {}\n\n".format(request.POST['tracking_code']))
			
			return HttpResponseRedirect("/track/{}".format(request.POST['tracking_code']))

		return HttpResponseRedirect("/track")

	def get_context_data(self,**kwargs):

		context = super().get_context_data(**kwargs)
		
		context['track_no'] = ""

		if(kwargs):

			try:
				context['itrack'] = TrackingDetails.objects.filter(trackcode=kwargs['tracking_code'])
			except TrackingDetails.DoesNotExist:
				pass

			#print("\n\n\n\n\nTracking Code:\n{}-1\n\n\n".format(kwargs['tracking_code']))
			context['track_no'] = kwargs['tracking_code']
		


		return context

def bad_request(request,exception):
	return render(request, 'errors/bad_request.html')		

def permission_denied(request,exception):
	return render(request, 'errors/permission_denied.html')		

def not_found(request,exception):
	return render(request, 'errors/not_found.html')		

def server_error(request):
	return render(request, 'errors/server_error.html')		

