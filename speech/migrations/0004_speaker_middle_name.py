# Generated by Django 3.1.7 on 2021-02-24 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speech', '0003_speaker_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]