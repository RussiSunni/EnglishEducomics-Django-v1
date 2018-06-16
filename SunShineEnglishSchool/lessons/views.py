from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question



def index(request):
    return render(request, 'lessons/index.html')

def welcome(request):
    return render(request, 'lessons/welcome.html')

def home_screen(request):
    return render(request, 'lessons/home_screen.html')

def achievements(request):
    return render(request, 'lessons/achievements.html')

def useful_vocabulary(request):
    return render(request, 'lessons/useful_vocabulary.html')

def travelling(request):
    return render(request, 'lessons/travelling.html')

def travelling_Fish_people_quest(request):
    return render(request, 'lessons/travelling-Fish_people_quest.html')

def quests(request):
    return render(request, 'lessons/quests.html')

def fish_person_hello(request):
    return render(request, 'lessons/fish_person_hello.html')

def outside(request):
    return render(request, 'lessons/outside.html')

def outside_Fish_people_quest(request):
    return render(request, 'lessons/outside-Fish_people_quest.html')

def map_screen(request):
    return render(request, 'lessons/map_screen.html')

def Fisherhaven(request):
    return render(request, 'lessons/Fisherhaven.html')

def Fish_people_quest(request):
    return render(request, 'lessons/Fish_people_quest.html')

def thisway(request):
    return render(request, 'lessons/thisway.html')










