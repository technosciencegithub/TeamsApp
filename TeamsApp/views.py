from django.db import IntegrityError

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView

from .models import Team, Player, GameScore
from .forms import AddTeamForm, AddTeamModelForm, AddScore, AddPlayerModelForm


class HomePageView(View):
    def get(self, request):
        teams = Team.objects.all()
        context = {'teams': teams}
        return render(request, 'team_list.html', context)


class TeamsListView(ListView):
    model = Team
    template_name = 'team_list.html'
    context_object_name = 'teams'





class ScoresListView(View):
    def get(self, request):
        scores = GameScore.objects.all()
        context = {'scores': scores , 'form': AddScore()}
        return render(request, 'score_list.html', context)
    def post(self, request):
        form = AddScore(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/scores/')


class ScoresListView1(ListView):
    model = GameScore
    template_name = 'score_list.html'
    context_object_name = 'scores'

    def get_context_data(self, **kwargs):
        context = super(ScoresListView1, self).get_context_data(**kwargs)
        context['form'] = AddScore()
        return context

    def post(self, request):
        form = AddScore(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/scores/')





class TeamDetailView(DetailView):
    model = Team
    template_name = 'team_detail.html'
    context_object_name = 'team'
    slug_field = 'name'





class PlayerDetailView(DetailView):
    model = Player
    template_name = 'player_detail.html'
    context_object_name = 'player'
    slug_field = 'name'





class AddTeamView(View):
    def get(self, request):
        context = {'form': AddTeamModelForm()}
        return render(request, 'add_team.html', context)

    def post(self, request):
        form = AddTeamModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context = {'form': form}
            return render(request, 'add_team.html', context)


class AddPlayerView(View):
    def get(self, request):
        context = {'form': AddPlayerModelForm()}
        return render(request, 'add_player.html', context)

    def post(self, request):
        form = AddPlayerModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context = {'form': form}
            return render(request, 'add_player.html', context)


