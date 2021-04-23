from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Training, TrainingImages,  TrainingVideo
# from micro.models import UserProfile
# from .forms import 

def all_training(request):
    training = Training.objects.order_by('-date')
    return render(request, 'training/all_training.html', {'trainings':training})

def detail(request, post_id):
    if request.method == 'POST':
        pass
        # cf = CommentForm(request.POST or None)
        # if cf.is_valid():
            # uav = get_object_or_404(UavPost, pk=post_id)
            # content = request.POST.get('content')
            # comment = Comment.objects.create(post = uav, user = request.user, content = content)
            # comment.save()
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        # cf = CommentForm()
        train = get_object_or_404(Training, pk=post_id)
        photos = TrainingImages.objects.filter(post=post_id)
        # comment = Comment.objects.filter(post=post_id)
        videos = TrainingVideo.objects.filter(post=post_id)
        return render(request, 'training/detail.html',{'train':train, 'photos':photos, 'videos':videos,})
