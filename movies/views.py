from django.http.response import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404,reverse
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
# Create your views here.

def index(request):
    movies = Movie.objects.filter(is_active=True,is_active_home=True)
    
    context = {
        'movies': movies
    }
    return render(request,'movies/index.html',context)

def movies(request):
    movies_active = Movie.objects.filter(is_active=True)
    
    context = {
        'movies_active': movies_active
    }
    return render(request,'movies/movies.html',context)

@login_required(login_url='login')
def movie_details(request,slug):
    movie_detail_slug = get_object_or_404(Movie,slug=slug)        
    genres = movie_detail_slug.genres.all()
    peoples = movie_detail_slug.people.all()
    videos = movie_detail_slug.video_set.all()
    # return HttpResponse(f"Detail Page with film slug {slug}")
    
    #?Yorum Yapilmasi
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie_detail_slug
            comment.save()
            return redirect(reverse('moviedetail',kwargs={'slug':slug}))
    else:
        comment_form = CommentForm()    
    
    context = {
        'movie_detail_slug':movie_detail_slug,
        'genres':genres,
        'peoples': peoples,
        'videos':videos,
        'comment_form':comment_form,
        'comments_all':movie_detail_slug.yorumlar.all()
    }
    
    return render(request,'movies/movie-detail.html',context)


    