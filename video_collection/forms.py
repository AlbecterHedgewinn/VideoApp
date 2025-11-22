from django import forms
from .models import Video

# create video form
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'url', 'notes']