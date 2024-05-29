# Generated by Django 5.0.6 on 2024-05-29 00:44

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_options_alter_user_data_nascimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pais',
            field=django_countries.fields.CountryField(db_column='pais', help_text='Informe o país', max_length=2, verbose_name='País'),
        ),
    ]