# Generated by Django 4.0 on 2022-03-13 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0011_publicacao_descricao_publicacao_hora_publicacao_tag_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacao',
            name='imagem',
            field=models.ImageField(default=None, upload_to='arquivos'),
            preserve_default=False,
        ),
    ]
