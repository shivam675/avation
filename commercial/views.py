from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Commercial, CommercialImages,  CommercialVideo, LearnPoints
# from micro.models import UserProfile
# from .forms import 

def all_commercial(request):
    commercials = Commercial.objects.order_by('-date')
    return render(request, 'commercial/all_commercial.html', {'commercials':commercials})

def detail(request, post_id):
    comm = get_object_or_404(Commercial, pk=post_id)
    points = LearnPoints.objects.filter(post=post_id)
    photos = CommercialImages.objects.filter(post=post_id)
    videos = CommercialVideo.objects.filter(post=post_id)
    return render(request, 'commercial/detail.html',{'comm':comm, 'photos':photos, 'videos':videos, 'points':points,})
    
