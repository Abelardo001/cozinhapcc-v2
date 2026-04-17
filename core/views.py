from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Carrossel, Prato, Ecomendas, Equipe, Cargo, Depoimento
from django.shortcuts import redirect 
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        busca = self.request.GET.get('q', '').strip()
        pratos = Prato.objects.all()

        if busca:
            pratos = pratos.filter(
                Q(nome__icontains=busca) | Q(descricao__icontains=busca)
            )

        context['busca'] = busca
        context['pratos'] = pratos.order_by('?')
        context['depoimento'] = Depoimento.objects.order_by('?').all()
        context['equipe'] = Equipe.objects.order_by('?').all()
        context['carrossel'] = Carrossel.objects.order_by('?').all()
        return context
