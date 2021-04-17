from django.contrib import admin

# Register your models here.
from .models import UavPost, UavImages, Comment

class PostUavImageAdmin(admin.StackedInline):
    model = UavImages

class PostUavCommentAdmin(admin.StackedInline):
    model = Comment


@admin.register(UavPost)
class PostUavAdmin(admin.ModelAdmin):
    inlines = [PostUavImageAdmin]

    class Meta:
        model = UavPost

# @admin.register(UavImages)
# class PostUavImageAdmin(admin.ModelAdmin):
#     pass

@admin.register(Comment)
class PostUavCommentAdmin(admin.ModelAdmin):
    pass
