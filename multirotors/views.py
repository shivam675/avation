from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import mRotorsPost, mRotorsImages, mRotorsComment, mRotorsVideo
# from micro.models import UserProfile
from .forms import CommentForm

def all_mRotors(request):
    mRotors = mRotorsPost.objects.order_by('-date')
    return render(request, 'all_mRotors.html', {'mRotors':mRotors})

def detail(request, post_id):
    if request.method == 'POST':
        cf = CommentForm(request.POST or None)
        if cf.is_valid():
            mRotors = get_object_or_404(mRotorsPost, pk=post_id)
            content = request.POST.get('content')
            comment = Comment.objects.create(post = mRotors, user = request.user, content = content)
            comment.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        cf = CommentForm()
        mRotors = get_object_or_404(mRotorsPost, pk=post_id)
        photos = mRotorsImages.objects.filter(post=post_id)
        comment = mRotorsComment.objects.filter(post=post_id)
        videos = mRotorsVideo.objects.filter(post=post_id)
        return render(request, 'detail.html',{'mRotors':mRotors, 'photos':photos, 'videos':videos, 'comments':comment ,'comment_form':cf})