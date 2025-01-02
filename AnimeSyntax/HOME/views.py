from django.shortcuts import render, get_object_or_404
from .models import Anime

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

def profile(request):
    return render(request, 'user-profile.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def home_page(request):
    recent_animes = Anime.objects.all().order_by('-created_at')[:5]
    

    return render(request, 'home_page.html', {
        'recent_animes': recent_animes,
    })


def anime_list(request):
    query = request.GET.get('q')
    if query:
        animes = Anime.objects.filter(title__icontains=query)
    else:
        animes = Anime.objects.all()
    return render(request, 'anime_list.html', {'animes': animes})

def anime_detail(request, anime_id):
    anime = get_object_or_404(Anime, pk=anime_id)
    return render(request, 'anime_detail.html', {'anime': anime})
