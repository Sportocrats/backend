# Generated by Django 3.2 on 2021-04-30 14:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sportocrats', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player_male',
            old_name='DOB',
            new_name='dob',
        ),
        migrations.RenameField(
            model_name='player_male',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='player_male',
            name='age',
        ),
        migrations.RemoveField(
            model_name='player_male',
            name='phone_no',
        ),
        migrations.AddField(
            model_name='player_male',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player_male',
            name='password',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player_male',
            name='sports',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]
