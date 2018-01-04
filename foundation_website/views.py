from django.shortcuts import render

def index(request):
    return render(request, 'foundation_website/index.html')

def contact(request):
    return render(request, 'foundation_website/contact.html')

def team(request):
    return render(request, 'foundation_website/team.html')

def medici(request):
    return render(request, 'foundation_website/projects/medici.html')
