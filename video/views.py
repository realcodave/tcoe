from django.shortcuts import render
from .models import Video
from operator import attrgetter
# Create your views here.

def video(request):

    video = sorted(Video.objects.all(), key=attrgetter('date_updated'), reverse=True)
    content = {"video": video}
    return render(request, "video/video.html", content)
