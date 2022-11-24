# Generated by Django 4.0.5 on 2022-11-24 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0008_livro_orientador_remove_livro_autor_livro_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='livros.autor'),
        ),
    ]