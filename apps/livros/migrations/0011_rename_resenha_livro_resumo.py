# Generated by Django 4.0.5 on 2022-11-24 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0010_rename_editora_livro_curso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='resenha',
            new_name='resumo',
        ),
    ]
