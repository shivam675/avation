from django.contrib import admin

# Register your models here.
from .models import UavPost, UavImages, Comment, UavVideo

class PostUavImageAdmin(admin.StackedInline):
    model = UavImages
    extra = 1

# class PostUavCommentAdmin(admin.StackedInline):
#     model = Comment
#     extra = 1

class PostUavVideoAdmin(admin.StackedInline):
    model = UavVideo
    extra = 1


# @admin.register(UavPost)
class PostUavAdmin(admin.ModelAdmin):
    inlines = [PostUavImageAdmin,
    PostUavVideoAdmin]
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
        model = UavPost

admin.site.register(UavPost, PostUavAdmin)


# @admin.register(UavImages)
# class PostUavImageAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Comment)
class PostUavCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post','created_at' ,'content')
    fieldsets = ((None,{'fields': ('post','user','content','created_at')}),)
    search_fields = ('user', 'post', 'content')

admin.site.register(Comment, PostUavCommentAdmin)
