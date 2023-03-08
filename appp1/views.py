from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def appp1(request):
    return HttpResponse('this is the first application')
