from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

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
        return HttpResponse(challenge)
    except:
        return HttpResponseNotFound("Entered month {} is not supported".format(month))
    

def month_id(request, monthid):
    try:
        month = list(monthly_challenge.keys())[monthid-1]        
        return HttpResponseRedirect('/challenges/'+month)
    except:
        return HttpResponseNotFound("challenges/"+str(monthid)+" is not supported")