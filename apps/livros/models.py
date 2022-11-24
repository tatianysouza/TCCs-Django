from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import *

class Autor(models.Model):
    nome = models.CharField(max_length=150, default=None, verbose_name="Primeiro nome:")
    unome = models.CharField(max_length=50, default=None, verbose_name="Último nome:")
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

class Orientador(models.Model):
    pnome = models.CharField(max_length=50, verbose_name="Primeiro nome:")
    unome = models.CharField(max_length=50, verbose_name="Último nome:")
    link_curriculo = models.URLField()

    def __str__(self):
        return self.pnome

class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    curso = models.ForeignKey(Editora, on_delete=models.PROTECT)
    ano_pub = models.IntegerField(verbose_name="Ano de publicação")
    resumo = models.TextField()
    tcc_pdf = models.FileField(upload_to='livros/', verbose_name="TCC em PDF")
    pchave = ArrayField(models.CharField(max_length=200), blank=True, verbose_name="Palavras Chave")
    capa = models.ImageField(upload_to='capas/', default=None)
    publicado = models.BooleanField(default=False, verbose_name="Publicar TCC")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    orientador = models.ForeignKey(Orientador, on_delete=models.PROTECT, null=True)

    class Meta():
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

