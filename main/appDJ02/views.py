from django.shortcuts import render

def index(request):
    return render(request, 'DJ02/index.html')

def basics(request):
    return render(request, 'DJ02/basics.html')

def equipment(request):
    return render(request, 'DJ02/equipment.html')

def tips(request):
    return render(request, 'DJ02/tips.html')

def safety(request):
    return render(request, 'DJ02/safety.html')
