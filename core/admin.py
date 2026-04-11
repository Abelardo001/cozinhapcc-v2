from django.contrib import admin
from core.models import Carrossel, Prato, Ecomendas, Equipe, Cargo, Depoimento


# Register your models here.
@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'ativo', 'criado', 'modificado')
    list_filter = ('ativo', 'criado', 'modificado')
    search_fields = ('nome', 'descricao')
@admin.register(Ecomendas)
class EcomendasAdmin(admin.ModelAdmin):
    list_display = ('prato', 'status', 'ativo', 'criado', 'modificado')
    list_filter = ('status', 'ativo', 'criado', 'modificado')
    search_fields = ('nome',)
@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'criado', 'modificado')
    list_filter = ('cargo', 'ativo', 'criado', 'modificado')
    search_fields = ('nome', 'nome')
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'criado', 'modificado')
    list_filter = ('ativo', 'criado', 'modificado')
    search_fields = ('nome',)
@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'criado', 'modificado')
    list_filter = ('ativo', 'criado', 'modificado')
    search_fields = ('nome', 'texto')
    list_per_page = 10
@admin.register(Carrossel)
class CarrosselAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ativo', 'criado', 'modificado')
    list_filter = ('ativo', 'criado', 'modificado')
    search_fields = ('titulo', 'descricao')