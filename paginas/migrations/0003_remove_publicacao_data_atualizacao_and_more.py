# Generated by Django 4.0 on 2022-03-07 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0002_delete_admin_publicacao_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacao',
            name='data_Atualizacao',
        ),
        migrations.AlterField(
            model_name='publicacao',
            name='hora',
            field=models.DateField(auto_now_add=True),
        ),
    ]
