from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# from django.template.loader import render_to_string

# Create your views here.
monthly_challenge = {
    'january'   :  'Its January. Eat no meat in the month',
    'february'  : 'Its February, Walk for 30 minutes everyday',
    'march'     : 'Its March. Practice Django for 30 mins everyday',
    'april'     : 'Its April. Eat no meat in the month',
    'may'       : 'Its May, Walk for 30 minutes everyday',
    'june'      : 'Its June. Practice Django for 30 mins everyday',
    'july'      :  'Its July. Eat no meat in the month',
    'august'    : 'Its August, Walk for 30 minutes everyday',
    'september' : 'Its September. Practice Django for 30 mins everyday',
    'october'   :  'Its October. Eat no meat in the month',
    'november'  : 'Its November, Walk for 30 minutes everyday',
    'december'  : 'Its December. Practice Django for 30 mins everyday',
}


def index(request, month):
    try:
        challenge = monthly_challenge[month]
        challengeText = "<h1>{}</h1>".format(challenge)
        return render(request, 'challenges/challenge.html', {
            'text': monthly_challenge[month],
            'month': month.capitalize(),
        })
        # challengeText = render_to_string("challenges/challenge.html")
        # return HttpResponse(challengeText)
    except:
        return HttpResponseNotFound("<h1>Entered month {} is not supported</h1>".format(month))
    

def month_id(request, monthid):
    try:
        month = list(monthly_challenge.keys())[monthid-1]
        redirect_path = reverse('month-challenge', args=[month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("<h1>challenges/{} is not supported</h1>".format(monthid))

def menu(request):
    menuItems = '<ul>'
    for month in list(monthly_challenge.keys()):
        monthPath = reverse('month-challenge', args=[month])
        menuItems += '<li> <a href = "{monthPath}"> {month}</a> </li>'.format(monthPath = monthPath, month = month)
    menuItems += '</ul>'
    return HttpResponse(menuItems)