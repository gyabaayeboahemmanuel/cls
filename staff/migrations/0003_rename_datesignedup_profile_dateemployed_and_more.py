# Generated by Django 4.0.3 on 2023-06-16 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_remove_profile_bio_remove_profile_blog_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='dateSignedUp',
            new_name='dateEmployed',
        ),
        migrations.AddField(
            model_name='profile',
            name='position',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Position'),
        ),
    ]