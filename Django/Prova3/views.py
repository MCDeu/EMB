from django.shortcuts import render
from data.utils import *

def principal(request):
    if request.method == 'POST':
        if request.POST.get("Clean") == "Clean":
            cleanMainKML()
            cleanSecundaryKML()            
            
    return render(request, 'principal.html', {})
