# Generated by Django 3.2.4 on 2021-06-13 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='sinopsis',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='capitulos',
            field=models.IntegerField(verbose_name='Capítulos'),
        ),
    ]
