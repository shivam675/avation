from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import ModelBulid, ModelImages, ModelVideo, LearnPoints
# from micro.models import UserProfile
# from .forms import 

def all_modelling(request):
    modelling = ModelBulid.objects.order_by('-date')
    return render(request, 'modelling/all_modelling.html', {'modellings':modelling})

def detail(request, post_id):
    modelbuild = get_object_or_404(ModelBulid, pk=post_id)
    points = LearnPoints.objects.filter(post=post_id)
    photos = ModelImages.objects.filter(post=post_id)
    videos = ModelVideo.objects.filter(post=post_id)
    return render(request, 'modelling/detail.html',{'modelbuild':modelbuild, 'photos':photos, 'videos':videos, 'points':points,})
    
