from django.shortcuts import render, HttpResponse

# Create your views here.

context = {
    'movies': ['gladiator', 'top_guns', 'casino']
}


def index(request):
    return render(request, 'movies/index.html', context)


def about(request):
    return render(request, 'movies/about.html', {})
