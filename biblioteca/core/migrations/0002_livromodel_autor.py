# Generated by Django 4.2.6 on 2023-11-02 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livromodel',
            name='autor',
            field=models.CharField(default='autor', max_length=200, verbose_name='autor'),
            preserve_default=False,
        ),
    ]
