from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.

LISTA_CATEGORIAS = (
    ("CULTOS", "Cultos"),
    ("MOVER_DO_ESPIRITO_SANTO", "Mover do Espirito Santo"),
    ("PREGACOES", "Pregações"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
    ("DISCIPULADO", "Discipulado"),
)


# criar estudos
class Estudo(models.Model): # Filme
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_estudos')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=25, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.titulo

# criar os episodios
class Episodio(models.Model):
    estudo = models.ForeignKey("Estudo", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()


    def __str__(self):
        return self.estudo.titulo + " - " + self.titulo


# criar usuário

class Usuario(AbstractUser):
    estudos_vistos = models.ManyToManyField("Estudo")