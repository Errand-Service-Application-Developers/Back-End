# Generated by Django 4.2.3 on 2023-07-24 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('errand', '0003_remove_user_expopushtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='listitem',
            name='job_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
    ]
