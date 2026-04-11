
from django.db import models
from stdimage.models import StdImageField
# Create your models here.

class BaseModel(models.Model):
    criado  = models.DateTimeField('criaçao', auto_now_add=True)
    modificado= models.DateTimeField('atualizado', auto_now=True)
    ativo   = models.BooleanField('ativo', default=True)

    class Meta:
        abstract = True

class Prato(BaseModel):
    nome = models.CharField('nome', max_length=100)
    descricao = models.TextField('descrição', max_length=500)
    preco = models.DecimalField('preço', max_digits=6, decimal_places=2)
    foto = StdImageField('Foto', upload_to='equipe', variations={'thumb': (300, 300)})

    class Meta:
        verbose_name = 'Prato'
        verbose_name_plural = 'Pratos'

    def __str__(self):
        return self.nome
STATUS_CHOICES = [
    ('P', 'Pendente'),
    ('C', 'Concluído'),
]
class Ecomendas(BaseModel):
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE, verbose_name='prato')
    status = models.CharField('status', max_length=1, choices=STATUS_CHOICES, default='P')
    
    class Meta:
        verbose_name = 'Encomenda'
        verbose_name_plural = 'Encomendas'

    def __str__(self):
        return self.prato.nome
class Equipe(BaseModel, ):
    nome = models.CharField('nome', max_length=100)
    cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE, verbose_name='cargo')
    foto = StdImageField('Foto', upload_to='equipe', variations={'thumb': (300, 300)})

    class Meta:
        verbose_name = 'Membro da Equipe'
        verbose_name_plural = 'Membros da Equipe'

    def __str__(self):
        return self.nome
class Cargo(BaseModel):
    nome = models.CharField('nome do cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.nome
class Depoimento(BaseModel):
    nome = models.CharField('nome do cliente', max_length=100)
    comentario = models.TextField('comentário', max_length=500)
    foto = StdImageField('Foto', upload_to='equipe', variations={'thumb': (300, 300)})
    cliente_desde = models.DateField('cliente desde', auto_now_add=True)

    inicio = models.DateField('data de início', auto_now_add=True)
    class Meta:
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'

    def __str__(self):
        return self.nome

class Carrossel(BaseModel):
    titulo = models.CharField('titulo', max_length=100)
    descricao = models.TextField('descrição', max_length=500)
    foto = StdImageField('Foto', upload_to='carrossel', variations={'thumb': (800, 600)})

    class Meta:
        verbose_name = 'Carrossel'
        verbose_name_plural = 'Carrosseis'

    def __str__(self):
        return self.titulo