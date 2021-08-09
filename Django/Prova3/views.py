from django.shortcuts import render

def principal(request):
    city=request.POST.get('')
    return render(request, 'principal.html', {})
