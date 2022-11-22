from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import *

class Autor(models.Model):
    nome = models.CharField(max_length=150, default=None)
    unome = models.CharField(max_length=50, default=None)
    foto = models.ImageField(upload_to="capas/", default=None)

    class Meta():
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Editora(models.Model):
    Modalidade = [
        ('Bacharelado', 'bacharelado'),
        ('Licenciatura', 'licenciatura'),
        ('Tecnológico', 'tecnológico')
    ]

    nome = models.CharField(max_length=150)
    modalidade = models.CharField(max_length=100, choices=Modalidade, null=True)

    class Meta():
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.ForeignKey()
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT)
    ano_pub = models.IntegerField(verbose_name="Ano de publicação")
    resenha = models.TextField()
    livro_pdf = models.FileField(upload_to='livros/', verbose_name="Livro em PDF")
    genero = ArrayField(models.CharField(max_length=200), blank=True)
    capa = models.ImageField(upload_to='capas/', default=None)
    publicado = models.BooleanField(default=False, verbose_name="Publicar livro")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta():
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

class Orientador(models.Model):
    pnome = models.CharField(max_length=50, verbose_name="Primeiro nome:")
    unome = models.CharField(max_length=50, verbose_name="Ultimo nome:")
    link_curriculo = models.URLField()

    def __str__(self):
        return self.pnome