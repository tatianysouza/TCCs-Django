# Generated by Django 4.0.5 on 2022-11-24 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0011_rename_resenha_livro_resumo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='livro_pdf',
            new_name='tcc_pdf',
        ),
    ]
