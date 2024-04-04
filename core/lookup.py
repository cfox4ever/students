import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import CustomUser


def autocomplete_username(request):
    users = CustomUser.objects.all()
    titles = list()
    for u in users :
        titles.append(u.username)

    
    return JsonResponse(titles,safe=False)
    