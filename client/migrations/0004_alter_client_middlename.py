# Generated by Django 4.0.3 on 2023-05-11 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_alter_client_middlename_alter_client_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='MiddleName',
            field=models.CharField(blank=True, default='.', max_length=255, null=True, verbose_name='Middle Name'),
        ),
    ]