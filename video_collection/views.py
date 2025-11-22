from django.shortcuts import render
from django.contrib import messages
from .views import VideoForm

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
            new_video_form.save()
            messages.info(request, 'New Video Saved!')
            # TODO show success message or redirect
        else:
            messages.warning(request, 'Please check the data entered.')
            return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})

    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})