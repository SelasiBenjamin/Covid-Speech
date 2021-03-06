# Generated by Django 3.1.7 on 2021-02-23 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speech', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speeches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('Post_Summary', models.TextField(help_text='Enter a brief description of the speech', max_length=1000)),
                ('date_of_post', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='date_of_death',
        ),
        migrations.DeleteModel(
            name='Speech',
        ),
        migrations.AddField(
            model_name='speeches',
            name='Speaker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='speech.speaker'),
        ),
    ]
