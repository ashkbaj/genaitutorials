from django.shortcuts import render
from django.http import HttpResponse
from . import models

moviesdetails1 = {
    "movies": [
        {
            'id': 5001,
            'name': "Jaws",
            'release': 1956
         },
        {
            'id': 5002,
            'name': "Sharknado",
            'release': 1960
        },
        {
            'id': 5003,
            'name': "The Meg",
            'release': 1966
        },
    ]
}
def home(request):
    return HttpResponse("This is my home page")

def movielist(request):
    data = models.Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': data})

def moviedetail(request, id):
    data = models.Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})