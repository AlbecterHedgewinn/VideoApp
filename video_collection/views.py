from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .forms import VideoForm
from .models import Video # Lets us query the database

# Create your views here.

# Create view for homepage
def home(request):
    app_name = 'Music Videos' # Put whatever videos you want here
    return render(request, 'video_collection/home.html', {'app_name': app_name})

# Add a view for adding a new video
def add(request):

    if request.method == 'POST':
        new_video_form = VideoForm(request.POST)
        if new_video_form.is_valid():
            try:
                new_video_form.save()
                return redirect('video_list')
                #   messages.info(request, 'New Video Saved!') # show success message
            except ValidationError:                         # Catch for incorrect url
                messages.warning(request, 'Invalid YouTube Url')
            except IntegrityError:                          # catch for potential copies in database
                messages.warning(request, 'You already added this video.')
        
        messages.warning(request, 'Please check the data entered.')
        return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})

    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_collection/video_list.html', {'videos': videos})
