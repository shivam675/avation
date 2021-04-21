from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import FixedWingPost, FixedWingImages, FixedWingVideo, FixedWingComment
# from micro.models import UserProfile
from .forms import CommentFormFixedwing

def all_fixedwing(request):
    fixs = FixedWingPost.objects.order_by('-date')
    return render(request, 'fixedwing/all_fixedwing.html', {'fixs':fixs})

def detail(request, post_id):
    if request.method == 'POST':
        cf = CommentFormFixedwing(request.POST or None)
        if cf.is_valid():
            fixedwing = get_object_or_404(UavPost, pk=post_id)
            content = request.POST.get('content')
            comment = Comment.objects.create(post = fixedwing, user = request.user, content = content)
            comment.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        cf = CommentFormFixedwing()
        fix = get_object_or_404(FixedWingPost, pk=post_id)
        photos = FixedWingImages.objects.filter(post=post_id)
        comment = FixedWingComment.objects.filter(post=post_id)
        videos = FixedWingVideo.objects.filter(post=post_id)
        return render(request, 'fixedwing/detail.html',{'fix':fix, 'photos':photos, 'videos':videos, 'comments':comment ,'comment_form':cf})
