from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/details.html', {'movie': movie})


def addMovie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MovieForm()

        return render(request, 'movies/Movie_form.html', {'form': form})
