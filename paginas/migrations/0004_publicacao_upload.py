# Generated by Django 4.0 on 2022-03-08 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0003_remove_publicacao_data_atualizacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacao',
            name='upload',
            field=models.FileField(default=1, upload_to='midia/'),
            preserve_default=False,
        ),
    ]
