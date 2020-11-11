from django.http import request
from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request, 'cms/admin_pan.html')


def delivery(request):
    return render(request, 'cms/delivery_day.html')


def run(request):
    return render(request, 'cms/run.html')
