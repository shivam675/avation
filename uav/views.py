from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import UavPost, UavImages, Comment, UavVideo
# from micro.models import UserProfile
from .forms import CommentForm

def all_uavs(request):
    uav = UavPost.objects.order_by('-date')
    return render(request, 'uav/all_uavs.html', {'uavs':uav})

def detail(request, post_id):
    if request.method == 'POST':
        cf = CommentForm(request.POST or None)
        if cf.is_valid():
            uav = get_object_or_404(UavPost, pk=post_id)
            content = request.POST.get('content')
            comment = Comment.objects.create(post = uav, user = request.user, content = content)
            comment.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        cf = CommentForm()
        uav = get_object_or_404(UavPost, pk=post_id)
        photos = UavImages.objects.filter(post=post_id)
        comment = Comment.objects.filter(post=post_id)
        videos = UavVideo.objects.filter(post=post_id)
        return render(request, 'uav/detail.html',{'uav':uav, 'photos':photos, 'videos':videos, 'comments':comment ,'comment_form':cf})
