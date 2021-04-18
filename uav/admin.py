from django.contrib import admin

# Register your models here.
from .models import UavPost, UavImages, Comment, UavVideo

class PostUavImageAdmin(admin.StackedInline):
    model = UavImages

class PostUavCommentAdmin(admin.StackedInline):
    model = Comment

class PostUavVideoAdmin(admin.StackedInline):
    model = UavVideo

@admin.register(UavPost)
class PostUavAdmin(admin.ModelAdmin):
    inlines = [PostUavImageAdmin,
    PostUavVideoAdmin]
    class Meta:
        model = UavPost

# @admin.register(UavImages)
# class PostUavImageAdmin(admin.ModelAdmin):
#     pass

@admin.register(Comment)
class PostUavCommentAdmin(admin.ModelAdmin):
    pass
