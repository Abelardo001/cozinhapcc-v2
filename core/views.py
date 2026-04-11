from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Carrossel, Prato, Ecomendas, Equipe, Cargo, Depoimento
from django.shortcuts import redirect 
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pratos'] = Prato.objects.order_by('?').all()
        context['depoimento'] = Depoimento.objects.order_by('?').all()
        context['equipe'] = Equipe.objects.order_by('?').all()
        context['carrossel'] = Carrossel.objects.order_by('?').all()
        return context
