from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class IndexPageView(TemplateView):
		template_name = 'index.html'

class ProvaPageView(TemplateView):
		template_name = 'prova.html'

