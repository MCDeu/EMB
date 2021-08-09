from django.shortcuts import render

def principal(request):
    city=request.POST.get('hola')
    return render(request, 'principal.html', {})