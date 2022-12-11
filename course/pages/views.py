from django.shortcuts import render



def mainPageView(request):
    return render(request, "main.html")

def filmsPageView(request):
    return render(request, "movies.html")

def cartoonsPageView(request):
    return render(request, "cartoons.html")

def serialsPageView(request):
    return render(request, "serials.html")

def animePageView(request):
    return render(request, "anime.html")

def accountPageView(request):
    return render(request, "account.html")