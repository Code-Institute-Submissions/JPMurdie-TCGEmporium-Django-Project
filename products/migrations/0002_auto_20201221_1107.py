# Generated by Django 3.1.4 on 2020-12-21 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mtg_cards',
            name='oracle_text',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]