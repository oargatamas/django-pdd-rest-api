from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def all_ppd(request):
    return HttpResponse("all")

def all_ppd_in_period(request, from_period, until_period):
    return HttpResponse("period: " + from_period + " to " + until_period)

def ppd_by_id(request, unique_id):
    return HttpResponse("by id: " + unique_id)