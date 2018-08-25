from django.db import models

# Create your models here.
import django.db.models.deletion


class Team(models.Model):
    name = models.CharField(max_length=256, unique=True)
    details = models.TextField()

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=256)
    number = models.IntegerField(default=0)
    age = models.IntegerField(default=18)
    position_in_field = models.CharField(max_length=256,
                                         choices=(('1', 'حارس'), ('2', 'دفاع'), ('3', 'وسط'), ('4', 'هجوم')))
    is_captain = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=django.db.models.deletion.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.name, self.team)


class GameScore(models.Model):
    team1 = models.ForeignKey(Team, related_name='first_team', on_delete=django.db.models.deletion.CASCADE)
    team2 = models.ForeignKey(Team, related_name='second_team', on_delete=django.db.models.deletion.CASCADE)
    first_team_score = models.IntegerField(default=0)
    second_team_score = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '{} {} - {} {}'.format(self.team1.name, self.first_team_score, self.second_team_score, self.team2.name)
