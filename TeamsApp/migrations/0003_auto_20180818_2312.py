# Generated by Django 2.1 on 2018-08-18 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeamsApp', '0002_auto_20180818_2304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamescore',
            old_name='game_date',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='gamescore',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_team', to='TeamsApp.Team'),
        ),
        migrations.AlterField(
            model_name='gamescore',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_team', to='TeamsApp.Team'),
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeamsApp.Team'),
        ),
    ]
