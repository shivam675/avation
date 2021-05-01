from django.contrib import admin

# Register your models here.
from .models import mRotorsPost, mRotorsImages, mRotorsComment, mRotorsVideo

class PostmRotorsImagesAdmin(admin.StackedInline):
    model = mRotorsImages
    extra = 1

# class PostUavCommentAdmin(admin.StackedInline):
#     model = Comment
#     extra = 1

class PostmRotorsVideoAdmin(admin.StackedInline):
    model = mRotorsVideo
    extra = 1


# @admin.register(mRotorsPost)
class PostmRotorsAdmin(admin.ModelAdmin):
    inlines = [PostmRotorsImagesAdmin,
    PostmRotorsVideoAdmin]
    list_display = ('title', 'user_name' , 'date','image')
    fieldsets = ((None,{'fields': (
    'title',
    'description',
    'image',
    'date',
    'Rotor_type',
    'RF_frequecy',
    'unit',
    'user_name',

    )}),)
    search_fields = ('title', 'user_name')
    class Meta:
        model = mRotorsPost

admin.site.register(mRotorsPost, PostmRotorsAdmin)


# @admin.register(UavImages)
# class PostUavImageAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Comment)
class mRotorsPostCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post','created_at' ,'content')
    fieldsets = ((None,{'fields': ('post','user','content',)}),)
    search_fields = ('user', 'post', 'content')

admin.site.register(mRotorsComment, mRotorsPostCommentAdmin)
