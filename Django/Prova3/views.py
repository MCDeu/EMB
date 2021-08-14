from django.shortcuts import render
from data.utils import *

def principal(request):
    if request.method == 'POST':
        if request.POST.get("Clean") == "Clean":
            cleanMainKML()
            cleanSecundaryKML()  
        if request.POST.get("Quit") == "Quit":
            removeEMBFolder()
            cleanMainKML()
            cleanSecundaryKML()  
            
    return render(request, 'principal.html', {})
