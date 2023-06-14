# Generated by Django 4.0.3 on 2023-05-12 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chief', '0004_remove_caretakerchief_chiefid_caretakerchief_id'),
        ('allocation', '0007_alter_allocation_caretakerchief'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocation',
            name='CareTakerChief',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='chief', to='chief.caretakerchief'),
        ),
    ]