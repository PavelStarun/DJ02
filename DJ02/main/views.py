from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def basics(request):
    return render(request, 'main/basics.html')

def equipment(request):
    return render(request, 'main/equipment.html')

def tips(request):
    return render(request, 'main/tips.html')

def safety(request):
    return render(request, 'main/safety.html')
