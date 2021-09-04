from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request, month):
    challenge = ''
    if month == 'january':
        challenge = 'Eat no meat for 30 days'
    elif month == 'february':
        challenge = 'walk for 30 mins evry day'
    elif month == 'march':
        challenge = 'Practice Django for 30 mins everyday'
    else:
        challenge = 'This month is not supported'
    return HttpResponse(challenge)

