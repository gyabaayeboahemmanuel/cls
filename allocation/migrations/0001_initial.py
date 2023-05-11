# Generated by Django 4.0.3 on 2023-03-25 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('chief', '0001_initial'),
        ('lands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiptno', models.CharField(max_length=255)),
                ('dateofallocation', models.DateField(auto_now=True)),
                ('CareTakerChief', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chief.caretakerchief')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('land', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lands.land')),
            ],
        ),
    ]