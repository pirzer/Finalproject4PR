# Generated by Django 3.2 on 2023-04-24 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Positive', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='positive',
            old_name='prep_time',
            new_name='championship_numbers',
        ),
        migrations.RenameField(
            model_name='positive',
            old_name='difficulty',
            new_name='impact',
        ),
        migrations.RenameField(
            model_name='positive',
            old_name='positivestory',
            new_name='pitch_the_story',
        ),
        migrations.RenameField(
            model_name='positive',
            old_name='cook_time',
            new_name='team_avg_playoffs',
        ),
        migrations.RenameField(
            model_name='positive',
            old_name='serves',
            new_name='team_avg_season',
        ),
        migrations.RenameField(
            model_name='positive',
            old_name='meal_image',
            new_name='team_image',
        ),
        migrations.RemoveField(
            model_name='positive',
            name='teams',
        ),
    ]