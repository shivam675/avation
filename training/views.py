from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Training, TrainingImages,  TrainingVideo, LearnPoints
# from micro.models import UserProfile
# from .forms import 

def all_training(request):
    training = Training.objects.order_by('-date')
    return render(request, 'training/all_training.html', {'trainings':training})

def detail(request, post_id):
    train = get_object_or_404(Training, pk=post_id)
    points = LearnPoints.objects.filter(post=post_id)
    photos = TrainingImages.objects.filter(post=post_id)
    videos = TrainingVideo.objects.filter(post=post_id)
    return render(request, 'training/detail.html',{'train':train, 'photos':photos, 'videos':videos, 'points':points,})
    
